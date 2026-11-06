# Carry arithmetic result

Full proof: [front_alpha/PROOFS.md](front_alpha/PROOFS.md), AC1–AC4. For B=16^m, C=1920/2457 and L=floor(log_B(15(A+1)^2/C))>=1, the number E of differences between the exact accumulated carry label and the initial B-adic cell label is at most m ceil(A/(mL)). Hence E=O_m(A/log A). Reset after a correction, followed by a positive upper recurrence, proves the exclusion spacing.

This is an unconditional original-forcing inequality, but holds for every seed. It is not class A in the requested sense. The carry and cell pressures differ by at most 2BE/A for fixed m. Both coherent and nearby periodic completions eventually have E=0 while their pressures grow at least B/p. Therefore corrections cannot pay the selected occupancy debt.

The missing count lies inside the E=0 population: chronological occurrences of equal K_m(n) modulo16^m. The literal zero boundary has not supplied a bound on this population. No selected numerator/cofactor cancellation was proved.
