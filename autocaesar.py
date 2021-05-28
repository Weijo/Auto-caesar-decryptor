#!/usr/bin/python3

"""
Caesar-cipher auto-decryptor on python

TODO:
1. Decryption algorithm   					[x]
2. Get entropy based on frequency analysis	[x]
3. Get all entropy 							[x]
5. Choose lowest entropy and decrypt 		[x]

Highly referenced from https://www.nayuki.io/page/automatic-caesar-cipher-breaker-javascript
"""
import math

def decrypt(string, key):
	if string == "":
		return
	
	result = ""
	for i in range(len(string)):
		char = string[i]

		if (char.isupper()): # Uppercase
			result += chr((ord(char) + key -65) % 26 + 65)
		elif (char.islower()): # Lowercase
			result += chr((ord(char) + key - 97) % 26 + 97)
		else: # Other characters
			result += char

	return result

def getEntropy(string):
	# Unigram model frequencies for letters A, B, ..., Z
	ENGLISH_FREQS = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,
		0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074,
	]

	summ = 0
	ignored = 0

	for i in range(len(string)):
		char = string[i]

		if (char.isupper()):
			summ += math.log(ENGLISH_FREQS[ord(char) - 65])
		elif (char.islower()):
			summ += math.log(ENGLISH_FREQS[ord(chars) - 97])
		else:
			ignored += 1

	return -summ / math.log(2) / (len(string) - ignored)

def getAllEntropies(string):
	results = []
	for i in range(26):
		results.append((i, getEntropy(decrypt(string, i))))
	return sorted(results, key = lambda x: x[1])

def main():
	test = 'ZNKT GRGJJOT MXGYVKJ ZNK XOTM OT ZNK CGE ZNK SGMOIOGT ZURJ NOS ZU JU'
	results = getAllEntropies(test)

	print(decrypt(test, results[0][0]))
	

if __name__ == "__main__":
	main()