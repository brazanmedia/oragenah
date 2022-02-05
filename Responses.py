from datetime import datetime

def sample_responses(input_text):
	user_message = str(input_text).lower()
	
	if user_message in ("bisa di swap","diswap","bisa swap"):
		return "Ke indomart beli minuman botol..\nGass swap toll..."

	if user_message in ("distri kapan","kapan distri"):
		return "Besok nunggu pengumuman..."

	if user_message in ("zonk","zong","zoonk"):
		return "Mampus..Tapi tenang..\nMasih ada ginjal"
