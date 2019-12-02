def my_csv_reader(fn: str, header=True, encoding='utf-8') -> list:
    """
    csv 파일의 데이터를 2차원 행렬 형태로 리턴

    :param fn: 읽을 csv 파일 이름(예: data\\exam.csv)
    :param header: csv 파일의 헤더 존재 여부
    :param encoding: 파일 인코딩
    :return: csv 파일에서 헤더는 제외한 데이터들로 이루어진 2차원 리스트
    """
    data = []  # 빈 리스트를 만든다.
    with open(fn, mode='r', encoding=encoding) as f:
        if header:  # csv 파일에 컬럼 이름들이 헤더에 있으면
            f.readline()  # 한 줄을 읽고 지나간다.
        for line in f:  # 파일 끝까지 한 줄씩 읽어서
            # 읽은 줄의 앞/뒤 공백문자를 제거하고(strip),
            # 문자열을 쉼표(,)로 분리(split)해서 문자열 리스트를 만들고,
            # 리스트 data에 추가한다.
            data.append(line.strip().split(','))

    return data
