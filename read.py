data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 100000 ==0 :
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')


# #以下把有提到nice的留言收集起來

# NICE = []
# # for message in data:
# # 	if 'nice' in message:
# # 		NICE.append(message)
# # print('總共有', len(NICE), '則留言提到 nice')
# # print(NICE[0])


# # 上方可以改寫成下面快寫法
# NICE = [message for message in data if 'nice' in message]
# print('總共有', len(NICE), '則留言提到 nice')
# print(NICE[0])


wc = {}
for d in data:
	words = d.split()	# split 預設是空白建，還不會切出多餘的空白 
	for word in words:
		if word in wc:
			wc[word] += 1
		else: 
			wc[word] = 1  # 新增新的詞進字典


# for key in wc:
# 	if wc[key] > 100:
# 		print(key, wc[key])

while True:
	word = input("請輸入你想查找的字:")
	if word == 'q':
		break
	elif word not in wc:
		print("沒有出現過此字")
	else:
		print(word, "在這群留言中出現過 ", wc[word], "次")
