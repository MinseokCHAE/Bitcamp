class CommonView(object):

    def print_dframe(self, dto):
        print('*' * 100)
        print('Check')
        print('*' * 100)
        print(f'1. type \n {type(dto)} ')
        print(f'2. column \n {dto.columns} ')
        print(f'3. head \n {dto.head()} ')
        print(f'4. null \n {dto.isnull().sum()} ')
        print('*' * 100)
