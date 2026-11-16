# Preregistered finite holdout (source-locked waves)

**This specification was written locally before executing X=360000.** Previous exploration used X=40000,120000,240000. A new fixed z=floor(cuberoot X) carrier X=360000 is evaluated with C++17 exact NTT and 64 direct integer pair-convolution checks. Required windows: [X/2,X] and [X,3X/2]. Required even residue classes modulo 12: 0,2,4,6,8,10.

**Finite predictions:** (i) every indicated class in each preregistered window has strictly positive signed aggregate, (ii) the ratio class-0/class-2 signed mass lies in [1.95,2.10] in both windows (the asymptotic CRT ratio is exactly 2), (iii) every integer-NTT sample agrees with the independent direct pair count, and (iv) any negative individual coefficient in other windows is retained and reported.

**Scope:** Prediction thresholds are empirical calibration bands, not consequences of an explicit effective N threshold for Siegel–Walfisz. No finite holdout proves a universal sign inequality. The semiprime cutoff is frozen at z=floor(cuberoot X), not the moving N-dependent z_N that defines the stronger conjecture.