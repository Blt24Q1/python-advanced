# import datetime
from datetime import datetime, date, time   # 특정 패키지(모듈) 내부의 객체


def get_datetime():
    """
    날짜와 시간 정보의 획득
    """

    # 현재 시간 -> now()
    now = datetime.now()
    print("현재시간:", now)

    # 생성자를 이용한 날짜의 지정
    # 년, 월, 일, 시, 분, 초, 마이크로세컨드
    # 최소 년, 월, 일
    dt = datetime(1999, 12, 31)
    print("1900년대 마지막 날:", dt)

    # 없는 날짜 지정하면 ValueError

    # datetime의 속성
    print(now.year, now.month, now.day,
          now.hour, now.minute, now.second, now.microsecond)

    # 요일정보 : 0-월 ~ 6-일
    print("요일:", now.weekday())

    # 날짜 정보를 반환 date() -> date 객체
    # 시간 정보를 반환 time() -> time 객체
    print("date:", now.date(), type(now.date()))  # 날짜정보
    print("time:", now.time(), type(now.time()))  # 시간정보

    # date 객체는 datetime 객체의 날짜관련 속성, 메서드
    d = now.date()
    print(d.year, d.month, d.day, d.weekday())
    # time 객체는 datetime 객체의 시간관련 속성, 메서드
    t = now.time()
    print(t.hour, t.minute, t.second, t.microsecond)


if __name__ == "__main__":
    get_datetime()