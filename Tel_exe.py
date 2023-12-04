Tels = {}

while True:
    help = '''====================Tel.exe============================
기능1 : 연락처 추가
기능2 : 연락처 전체 보기
기능3 : 검색, 이름을 입력받아서 전화번호 조회
기능4 : 수정, 이름을 입력받아서 전화번호 입력수정
기능5 : 삭제, 이름 입력받아서 삭제
기능6 : 프로그램 종료'''
    print(help) # 프로그램 시작시 help 출력
    Tel_exe = int(input('기능선택'))

    if Tel_exe == 1:
        #추가할 이름 (딕셔너리의 key값) 입력하기
        print('추가할 이름을 입력하세요')
        add_name = input('추가할 이름')
        #추가할 이름 (딕셔너리의 value값) 입력하기
        print('추가할 전화번호를 입력하세요')
        add_Tel = input('추가할 전화번호')
        #input값으로 새로운 딕셔너리 key,value 추가하기
        Tels[add_name] = add_Tel

    elif Tel_exe == 2:
        #현재 Tels 딕셔너리 상태 출력
        for name, Telnum in Tels.items():
            print(name, Telnum)

    elif Tel_exe == 3:
        print('검색할 이름을 입력하세요')
        # while문을 입력하여 잘못입력할경우 다시 입력하기
        while True:
            search_name = input('이름')
            if search_name in Tels.keys():
                print(f'{search_name} : {Tels[search_name]}')
                break
            else:
                print('존재하지 않는 이름입니다')

    elif Tel_exe == 4:
        print('수정할 연락처의 이름을 입력하세요')
        while True:
            search_name = input('수정하고싶은 이름')
            if search_name in Tels.keys():
                print(f'{search_name}을 어떻게 수정할까요?')
                break
            else:
                print('존재하지 않는 이름입니다')
        update_name = input('새로운 이름')
        Tels[update_name] = Tels[search_name]
        print('연락처는 어떻게 수정할까요?')
        update_num = input('수정할 연락처')
        Tels[update_name] = update_num
        del Tels[search_name]
        print(f'{search_name}이 {update_name}:{Tels[update_name]}으로 변경되었습니다')

    elif Tel_exe == 5:
        print('삭제할 이름을 입력하세요')
        while True:
            search_name = input('삭제하고싶은 이름')
            if search_name in Tels.keys():
                del Tels[search_name]
                print(f'{search_name}이 삭제되었습니다')
                break
            else:
                print('존재하지 않는 이름입니다')

    elif Tel_exe == 6:
        print('작업을 종료합니다')
        break

    else:
        print('1부터 6까지의 숫자를 입력해주세요')
