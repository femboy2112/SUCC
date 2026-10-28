"""Check local links/delimiters and GitHub's actual GFM math recognition."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
FILES=[ROOT/name for name in (
    'research/2026-10-27/CARRY_DEFECT_SYNTHESIS.md',
    'research/2026-10-27/PERIODIC_TEMPLATE_COERCIVITY.md',
    'research/2026-10-27/MIXED_LAG_PERIODIC_COERCIVITY.md',
    'research/2026-10-27/MIXED_LAG_REVIEW.md',
    'research/2026-10-27/CARRY_DEFECT_ENERGY.md',
    'research/2026-10-27/CARRY_DEFECT_VALIDATION.md',
    'docs/CLAIM_SUPPLEMENT_CARRY_DEFECT.md',
    'handoffs/CARRY_DEFECT_NEXT_PI_2026-10-27.md',
)]


class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.math=0
        self.tables=[]
        self.row=None
        self.math_depth=0
        self.code_depth=0
        self.unrendered=[]
    def handle_starttag(self,tag,attrs):
        if tag=='math-renderer':
            self.math+=1
            self.math_depth+=1
        if tag in ('code','pre'):self.code_depth+=1
        if tag=='tr':self.row=0
        if tag in ('td','th') and self.row is not None:self.row+=1
    def handle_data(self,data):
        if '$' in data and not self.math_depth and not self.code_depth:
            self.unrendered.append(data)
    def handle_endtag(self,tag):
        if tag=='math-renderer':self.math_depth-=1
        if tag in ('code','pre'):self.code_depth-=1
        if tag=='tr':
            self.tables.append(self.row)
            self.row=None


def main():
    results=[]
    for path in FILES:
        source=path.read_text()
        if source.count('$$')%2:
            raise SystemExit(f'unpaired display math: {path}')
        if re.search(r'\\[\[\]()]',source):
            raise SystemExit(f'unsupported math delimiter: {path}')
        for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',source):
            if '://' not in target and not target.startswith('#'):
                local=target.split('#')[0]
                if local and not (path.parent/local).exists():
                    raise SystemExit(f'broken local link: {path}: {target}')
        payload=json.dumps({'text':source,'mode':'gfm','context':'femboy2112/SUCC'})
        result=subprocess.run(['gh','api','--method','POST','markdown','--input','-'],
                              cwd=ROOT,input=payload,text=True,stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        if result.returncode:
            raise SystemExit(result.stderr)
        rendered=result.stdout
        audit=Audit()
        audit.feed(rendered)
        if audit.unrendered:
            raise SystemExit(f'unrendered math: {path}: {audit.unrendered}')
        # GitHub uses inline <span> or <div> with the math-renderer class.
        recognized=rendered.count('math-renderer')
        if '$' in source and not recognized:
            raise SystemExit(f'GitHub did not recognize math: {path}')
        if path.name=='CLAIM_SUPPLEMENT_CARRY_DEFECT.md':
            (OUT/'claim_table_rendered.html').write_text(rendered)
            if audit.tables != [4]*11:
                raise SystemExit(f'claim table column corruption: {audit.tables}')
        results.append({'path':str(path.relative_to(ROOT)),
                        'source_sha256':hashlib.sha256(source.encode()).hexdigest(),
                        'rendered_sha256':hashlib.sha256(rendered.encode()).hexdigest(),
                        'math_renderer_occurrences':recognized,
                        'table_row_column_counts':audit.tables})
    (OUT/'markdown_audit.json').write_text(json.dumps(results,indent=2)+'\n')
    print(f'GitHub rendered {len(results)} documents; links, delimiters and claim table passed')


if __name__=='__main__':main()
