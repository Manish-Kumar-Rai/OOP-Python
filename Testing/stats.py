from collections import defaultdict

# myList = [10, 2, 9, 6, 3, 6, 7, 2, 10, 5, 9, 5, 8, 1, 9, 9, 10, 3, 3, 4]

class StatsList(list):
    def mean(self):
        return sum(self)/len(self)
    
    def median(self):
        if len(self) % 2:
            return self[int(len(self) / 2)]
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx-1]) / 2
        
    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1

        max_freq = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == max_freq:
                modes.append(item)
        return modes