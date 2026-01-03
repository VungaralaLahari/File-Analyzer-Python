import string

class FileAnalyser():
    def read_file(self, filepath):
        with open(filepath, "r") as f:
            return f.read()

    def count_lines(self, data):
        return len(data.split("\n"))

    def count_words(self, data):
        return len(data.split())

    def count_characters(self, data):
        return len(data)

    def word_frequency(self, data):
        freq = {}
        for i in string.punctuation:
            data = data.replace(i, " ")
        words = data.lower().split()
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        return freq

    def top_words(self, freq, n=5):
        items = list(freq.items())
        items.sort(key=lambda x: x[1], reverse=True)
        return items[:n]


analyser = FileAnalyser()
data = analyser.read_file("sample.txt")

print("The Number of lines:", analyser.count_lines(data))
print("The Number of words:", analyser.count_words(data))
print("The Number of Characters:", analyser.count_characters(data))
print("The Words Frequencies:", analyser.word_frequency(data))
print("Top Frequent Words:", analyser.top_words(analyser.word_frequency(data)))
