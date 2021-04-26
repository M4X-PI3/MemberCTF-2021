# Gia tri dau tien cua password la gia tri thu 2 cua v7 -> bo 2 ky tu dau
v7 = "1pB__@!!s@11c!ccc_@rcss0!rm_spc_ac1ram3pB__m!_m!"

result = []
for i in range(0, len(v7), 3):
	result.append(v7[i+2])

print("Password: ", ''.join(result))