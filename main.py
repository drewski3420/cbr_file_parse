class CBRFile:
    def __init__(self, fn):
        self.file_name = fn
        self.result = self.run_file()
    def run_file(self):
        result = []
        with open(self.file_name, 'r') as f:
            data = f.read()
        split_data = data.split('\n')
        for line in split_data:
            try:
                loan_number = int(line[1:12])
                apd = int(line[100:107].replace(',', ''))
                if str(apd) == '0':
                    line_result = [loan_number, apd]
                    result.append(line_result)
            except:
                pass
        return result

def output_file(fn,result):
    with open(fn, 'w+') as f:
        f.write('loan_number, amt_past_due\n')
        for line in result:
            f.write('{},{}\n'.format(line[0], line[1]))

def main():
    file1 = CBRFile('t61r.txt')
    file2 = CBRFile('t61r2.txt')
    result = file1.result + file2.result
    output_file('output.csv', result)

if __name__ == '__main__':
    main()
