import pandas as pd
import numpy as np


if __name__ == '__main__':

    while 1:

        menu = int(input(
            '0.exit \n'
            '22.다음 객체에서 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출려되는 코드를 작성 \n'
            '23.다음 객체에서 행의 각 요소에서 행의 평균을 뺀 값을 출력 \n'
            '24.다음 객체에서 가장 작은 합계를 가진 숫자열의 열을 출력 \n'
            '25.다음 객체에서 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..) \n'
            '26.객체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다. \n'
            '27.For each group, find the sum of the three greatest values. \n'
            '28.다음 객체를 list 로 변환하시오 \n'
            '29.다음 객체를 dictionary 로 변환하시오 \n'
            '30.다음 객체를 customer_id 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오 \n'
            '31.30번 객체를 customer_id 와 grade 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오'))

        def q22():
            # 22. 다음 객체에서 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출려되는 코드를 작성
            df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
            df = df.loc[df['A'].shift() != df['A']]
            return df

        def q23():
            # 23. 다음 객체에서 행의 각 요소에서 행의 평균을 뺀 값을 출력
            df = pd.DataFrame(np.random.random(size=(5, 3)))
            df.sub(df.mean(axis=1), axis=0)
            return df

        def q24():
            # 24. 다음 객체에서 가장 작은 합계를 가진 숫자열의 열을 출력
            df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
            return df.sum().idxmin()

        def q25():
            # 25. 다음 객체에서 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..)
            df = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))
            return len(df.drop_duplicates(keep=False))

        def q26():
            # 26. 객체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다.
            # 답은 e, c, d, h, d 입니다.
            nan = np.nan
            data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
                    [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
                    [nan, nan, 0.5, nan, 0.31, 0.4, nan, nan, 0.24, 0.01],
                    [0.49, nan, nan, 0.62, 0.73, 0.26, 0.85, nan, nan, nan],
                    [nan, nan, 0.41, nan, 0.05, nan, 0.61, nan, 0.48, 0.68]]
            columns = list('abcdefghij')
            df = pd.DataFrame(data, columns=columns)
            return (df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)

        def q27():
            # 27. For each group, find the sum of the three greatest values.
            # 출력 결과는
            #  grps
            #   a    409
            #   b    156
            #   c    345
            # 이렇게 나옵니다.
            df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                               'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
            return df.groupby('grps')['vals'].nlargest(3).sum(level=0)

        def q28():
            # 28. 다음 객체를 list 로 변환하시오
            df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
            return df.values.tolist()

        def q29():
            # 29. 다음 객체를 dictionary 로 변환하시오
            df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
            return df.to_dict()

        def q30():
            # 30. 다음 객체를 customer_id 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오
            df = pd.DataFrame({"customer_id": ['kim', 'lee', 'park', 'song', 'yoon', 'kang', 'tak', 'ryu', 'jang'],
                               "product_code": ['com', 'phone', 'tv', 'com', 'phone', 'tv', 'com', 'phone', 'tv'],
                               "grade": ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                               "purchase_amount": [30, 10, 0, 40, 15, 30, 0, 0, 10]})
            return pd.pivot_table(df, index='customer_id', columns='product_code', values='purchase_amount')

        def q31():
            # 31. 30번 객체를 customer_id 와 grade 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오
            df = pd.DataFrame({"customer_id": ['kim', 'lee', 'park', 'song', 'yoon', 'kang', 'tak', 'ryu', 'jang'],
                               "product_code": ['com', 'phone', 'tv', 'com', 'phone', 'tv', 'com', 'phone', 'tv'],
                               "grade": ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                               "purchase_amount": [30, 10, 0, 40, 15, 30, 0, 0, 10]})
            return pd.pivot_table(df, index=['customer_id', 'grade'], columns='product_code', values='purchase_amount')


        if menu == 0:
            break
        elif menu == 22:
            print(q22())
        elif menu == 23:
            print(q23())
        elif menu == 24:
            print(q24())
        elif menu == 25:
            print(q25())
        elif menu == 26:
            print(q26())
        elif menu == 27:
            print(q27())
        elif menu == 28:
            print(q28())
        elif menu == 29:
            print(q29())
        elif menu == 30:
            print(q30())
        elif menu == 31:
            print(q31())
        else:
            print('wrong input')
            continue
