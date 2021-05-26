
class VectorTest(object):

    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tiny_ls = [123, 'john']

    def ls_create(self):
        # Create: ls 에 '100'을 추가 Create

        self.ls.append(100)

    def ls_read(self):
        # Read: ls 의 목록을 출력

        print(self.ls)

    def ls_update(self):
        # Update: ls와 tinyls 의 결합

        self.ls.extend(self.tiny_ls)
        self.ls += self.tiny_ls

    def ls_delete(self):
        # Delete: ls 에서 786을 제거

        self.ls.remove(786)

    @staticmethod
    def main():
        v = VectorTest()

        while 1:
            menu = input('0.Exit 1.Create, 2.Read, 3.Update, 4.Delete')
            if menu == '0':
                break
            elif menu == '1':
                v.ls_create()
            elif menu == '2':
                v.ls_read()
            elif menu == '3':
                v.ls_update()
            elif menu == '4':
                v.ls_delete()
            else:
                continue

VectorTest.main()
