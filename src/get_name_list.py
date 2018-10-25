from pathlib import Path
import itertools

DIRNAME = "/Users/kei/GitHub/kuarchi-programming-2018/181005-class/181005attendance-10-12-2018-01-15-00"
# DIRNAME = r"C:\Users\o-kei\Documents\GitHub\kuarchi-programming-2018\181003attendance-studentrepos\181005attendance-10-10-2018-07-35-43"
# DIRNAME = r"C:\Users\o-kei\Documents\GitHub\kuarchi-programming-2018\181003attendance-studentrepos\181005attendance-10-12-2018-03-05-52"


def check_is_filename(path, filename):
    dirs = [x for x in path.iterdir() if x.is_dir()]
    for dir in dirs:
        filepath = dir / filename
        flag = filepath.exists()
        if not flag:
            print(dir)

if __name__ == '__main__':
    path = Path(DIRNAME)

    files = path.glob("*/profile.txt")

    ## count files
    files, files2 = itertools.tee(files) # clone generator
    print(len(list(files2)))

    # check_is_filename(path, "profile.txt")

    data = []
    columns = ['name', 'id', 'github', 'programming', 'PC', 'laptop', 'Q1', 'Q2']
    for file in files:
        data_line = []
        with file.open(encoding='utf-8', errors='ignore') as f:
            lines = list(f.readlines())
            for col, line in zip(columns, lines):
                line = line.strip()
                line_split = line.split(':')
                if len(line_split) == 1:
                    line_split.append('error')
                if col == 'id':
                    line_split[1] = line_split[1].strip().replace('-', '')
                    # print(line_split)
                if len(line_split) == 2:
                    data_line.append(line_split[1])
        data.append(','.join(data_line))
            # lines = f.readlines()
            # for line in lines:
            #     print(line)
            #     if '氏名' in line:
            #         dic[name] = line.strip(':')[1]
                # print(line.split(':'))
    
    path_w = 'data.csv'
    with open(path_w, mode='w', encoding='shift_jis',errors='ignore') as f:
        f.writelines(','.join(columns) + '\n')
        f.writelines('\n'.join(data))