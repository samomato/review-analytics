data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 ==0 :
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

#以下把有提到nice的留言收集起來

NICE = []
# for message in data:
# 	if 'nice' in message:
# 		NICE.append(message)
# print('總共有', len(NICE), '則留言提到 nice')
# print(NICE[0])


# 上方可以改寫成下面快寫法
NICE = [message for message in data if 'nice' in message]
print('總共有', len(NICE), '則留言提到 nice')
print(NICE[0])