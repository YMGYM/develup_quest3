# 작성자 maintain0404(민태인)
# 2019-11-19 작성
#TODO 에러핸들링이 되어 있지 않음

import datetime

class Event:
    # 이벤트 정보 객체
    # 날짜, 이름, 설명, 사진으로 구성
    # 설명과 날짜는 없어도 됨
    #TODO 데이터의 제약사항(크기, 형식) 등 정의해놓으면 좋겠다.
    def __init__(self, name : str, date : datetime.datetime, comment : str = None, picture = None):
        self.__name = name
        self.__date = date
        self.__comment = comment

        self.__picture = picture

    #데이터 식별을 위한 repr, 이름을 반환
    def __repr__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name : str):
        self.__name = name
    
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date : datetime.datetime):
        self.__date = date

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment : str):
        self.__comment = comment

    @property
    def picture(self):
        return self.__picture

    @picture.setter
    def getPicture(self, picture):
        self.__picture = picture

    def days_remaining(self):
        today = datetime.datetime.today()
        return (self.__date - today).days
        

class EventCalender:
    # 1. 설명이 지정되지 않은 경우 해결해야 함
    # 2. 삭제 시 한 번 더 확인한다고 했을 때, 확인 전/진짜 지울 떄 탐색이 두번 이뤄져야 함
    #TODO clear 3. 2를 해결하기 위해 모든 서치함수는 search_buffer에 결과를 저장하고 이 리스트를 반환함 서치시마다 버퍼는 갱신됨
    # 4. 현재 모든 서치함수는 브루트포스로 작성됨
    # 5. 삭제 불가능 지정이 필요할까?
    #TODO clear 6. 서치 버퍼 삭제는 개선할 수 있을 것 같다. -> 서치 버퍼엔 이벤트리스트 인덱스를,
    #              버퍼프로퍼티함수엔 실제 객체를 보여주기 방식으로 개선
    def __init__(self, lastday : Event):
        self.__eventlist = list() #일단 리스트, 성능 높일려면 iter, generater로 고치면 성능이 올라가지 않을까용
        self.__eventlist.append(lastday)
        self.__search_buffer = list()
         
    @property
    def eventlist(self):
        return self.__eventlist

    @property
    def eventcount(self):
        return len(self.__eventlist)

    @property
    def search_buffer(self):
        temp = []
        for i in self.__search_buffer:
            temp.append(self.__eventlist[i])
        return temp

    def add_event(self, event : Event):
        self.__eventlist.append(Event)

    def search_event(self, name : str = None, startdate : datetime.datetime = None, 
                enddate : datetime.datetime = None, comment : str = None):
        self.__search_buffer = []
        
        temp = []
        if name:
            for i in self.__eventlist:
                if name in i.name:
                    temp.append(i)
            self.__search_buffer = temp
        else:
            self.__search_buffer = self.__eventlist[:] # 새로 복제, 다 지워진다면 여기서 복제가 안됐을 가능성 높음
        
        temp = []
        if startdate:
            for i in self.__search_buffer:
                if (i.__date - startdate).days >= 0:
                    temp.append(self.__eventlist.index(i))
            self.__search_buffer = temp
        
        temp = []
        if enddate:
            for i in self.__search_buffer:
                if (enddate - i.__date).days >= 0:
                    temp.append(self.__eventlist.index(i))
            self.__search_buffer = temp
        
        temp = []
        if comment:
            for i in self.__search_buffer:
                if comment in i.comment:
                    temp.append(self.__eventlist.index(i))
            self.__search_buffer = temp

        return self.search_buffer # 이렇게 하는 게 맞는지 모르겠다

    def search_event_by_name(self, eventname : str):
        self.__search_buffer = []
        for i in self.__eventlist:
            if eventname in i.name:
                self.__search_buffer.append(self.__eventlist.index(i))
        return self.search_buffer # 이렇게 하는 게 맞는지 모르겠다

    def search_event_by_date(self, startdate : datetime.datetime, enddate : datetime.datetime):
        #시작일, 종료일과 일치해도 참
        self.__search_buffer = []
        for i in self.__eventlist:
            if (i.__date - startdate).days >= 0 and (enddate - i.__date).days >= 0:
                self.__search_buffer.append(self.__eventlist.index(i))
        return self.search_buffer # 이렇게 하는 게 맞는지 모르겠다
        
    def search_event_by_comment(self, comment : str):
        self.__search_buffer = []
        for i in self.__eventlist:
            if comment in i.comment:
                self.__search_buffer.append(self.__eventlist.index(i))
        return self.search_buffer # 이렇게 하는 게 맞는지 모르겠다
    
    def delete_event_by_name(self, eventname : str):
         for i in self.__eventlist:
            if eventname in i.name:
                del i #참조 해제, 다른 이름으로 참조 하지 않을 것

    def delete_event_by_date(self, startdate : datetime.datetime, enddate : datetime.datetime):
        #시작일, 종료일과 일치해도 참
        for i in self.__eventlist:
            if (i.__date - startdate).days >= 0 and (enddate - i.__date).days >= 0:
                del i

    def delete_event_by_comment(self, comment : str):
        for i in self.__eventlist:
            if comment in i.comment:
                del i

    def delete_search_buffer(self):
        #TODO 완전히 참조해제하는 코드 더 좋은 방법이 있을 것 같다
        temp = []
        for i in range(self.__eventlist):
            for j in range(self.__search_buffer):
                if self.__eventlist[i] is self.__search_buffer[j]:
                    temp.append((i, j))
        for k in temp:
            del self.__eventlist[k[0]]
            del self.__search_buffer[k[1]]

