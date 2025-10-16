#Otto Bauer Reproduction Scheme (Extended By Henryk Grossman) Sim

c0 = 200000 #initial constant capital
v0 = 100000 #initial variable capital
s = 1.0     #rate of surplus value
ac = 0.10   #accumulation rate of constant capital
av = 0.05   #accumulation rate of variable capital
years = 35

c = c0
v = v0

print(f"{'Year':<5} {'c':>10} {'v':>10} {'k':>10} {'ac*c':>10} {'av*v':>10} {'=':>3} {'Total':>10}")
print("-" * 65)

for year in range(1, years + 1):
    S = round(s * v)
    ac_c = round(ac * c)
    av_v = round(av * v)
    S_required = ac_c + av_v
    k = round(S - S_required)
    total = round(c) + round(v) + round(ac_c) + round(av_v) + round(max(0, k))

    print(f"{year:<5} {round(c):>10,} {round(v):>10,} {max(0, k):>10,} {ac_c:>10,} {av_v:>10,} {'=':>3} {total:>10,}")

    if k <= 0:
        deficit = abs(k)
        print(f"\nDeficit = {deficit:,}")
        print(f"Absolute crisis reached in year {year}")
        break

    c += ac_c
    v += av_v
