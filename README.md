# 깔끔한 파이썬 탄탄한 백엔드 
- 깔끔한 파이썬 탄탄한 백엔드 책의 내용 중 중요 챕터 위주로만 정리함
- 원활한 실행을 위해서 다음의 작업들을 수행
pyenv virtualenv를 이용한 가상환경 설정
```bash
pyenv virtualenv 3.7.7 flask101
pip install --upgrade pip
pip install -r requirements.txt
```
httpie 설치
```bash
brew install httpie # macOS일 경우
```
```bash
sudo apt install httpie # ubuntu일 경우
```
### 01. 파이썬 설치 및 개발 환경구성
1. 본격적인 설치에 앞서
2. 파이썬 설치
3. 파이썬 가상 환경 설치
4. 터미널 환경
5. 깃
6. [셸](https://github.com/aisolab/flask101/wiki/01-6.-%EC%85%B8)
7. 다양한 에디터 소개
### 02. 현대 웹 시스템 구조 및 아키텍쳐
1. 웹 시스템들의 발전 역사
2. 현대 웹 시스템들의 구조 및 아키텍쳐
3. 현대 개발팀의 구조
### 03. 첫 API 개발 시작
1. Flask
2. [시작도 첫걸음부터 - ping 엔드포인트 구현하기](https://github.com/aisolab/flask101/wiki/03-2.-%EC%8B%9C%EC%9E%91%EB%8F%84-%EC%B2%AB%EA%B1%B8%EC%9D%8C%EB%B6%80%ED%84%B0---ping-%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
3. [API 실행하기](https://github.com/aisolab/flask101/wiki/03-3.-API-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0)
### 04. HTTP의 구조 및 핵심 요소
1. HTTP
2. [HTTP 통신 방식](https://github.com/aisolab/flask101/wiki/04-2.-HTTP-%ED%86%B5%EC%8B%A0-%EB%B0%A9%EC%8B%9D)
3. [HTTP 요청 구조](https://github.com/aisolab/flask101/wiki/04-3.-HTTP-%EC%9A%94%EC%B2%AD-%EA%B5%AC%EC%A1%B0)
4. [HTTP 응답 구조](https://github.com/aisolab/flask101/wiki/04-4.-HTTP-%EC%9D%91%EB%8B%B5-%EA%B5%AC%EC%A1%B0)
5. [자주 사용되는 HTTP 메소드](https://github.com/aisolab/flask101/wiki/04-5.-%EC%9E%90%EC%A3%BC-%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94-HTTP-%EB%A9%94%EC%86%8C%EB%93%9C)
6. [자주 사용되는 HTTP Status Code와 Text](https://github.com/aisolab/flask101/wiki/04-6.-%EC%9E%90%EC%A3%BC-%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94-HTTP-Status-Code%EC%99%80-Text)
7. [API 엔드포인트 아키텍쳐 패턴](https://github.com/aisolab/flask101/wiki/04-7-API-%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8-%EC%95%84%ED%82%A4%ED%85%8D%EC%B3%90-%ED%8C%A8%ED%84%B4)
### 05. 본격적으로 API 개발하기
1. [미니터의 기능](https://github.com/aisolab/flask101/wiki/05-1.-%EB%AF%B8%EB%8B%88%ED%84%B0%EC%9D%98-%EA%B8%B0%EB%8A%A5)
2. [회원가입](https://github.com/aisolab/flask101/wiki/05-2.-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85)
3. [300자 제한 트윗 글 올리기](https://github.com/aisolab/flask101/wiki/05-3.-300%EC%9E%90-%EC%A0%9C%ED%95%9C-%ED%8A%B8%EC%9C%97-%EA%B8%80-%EC%98%AC%EB%A6%AC%EA%B8%B0)
4. [팔로우와 언팔로우 엔드포인트](https://github.com/aisolab/flask101/wiki/05-4.-%ED%8C%94%EB%A1%9C%EC%9A%B0%EC%99%80-%EC%96%B8%ED%8C%94%EB%A1%9C%EC%9A%B0-%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8)
5. [타임라인 엔드포인트](https://github.com/aisolab/flask101/wiki/05-5.-%ED%83%80%EC%9E%84%EB%9D%BC%EC%9D%B8-%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8)
6. [전체 코드](https://github.com/aisolab/flask101/wiki/05-6.-%EC%A0%84%EC%B2%B4%EC%BD%94%EB%93%9C)
### 06. 데이터베이스
1. [데이터베이스 시스템](https://github.com/aisolab/flask101/wiki/06-1.-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%8B%9C%EC%8A%A4%ED%85%9C)
2. [관계형 데이터베이스 시스템 VS 비관계형 데이터베이스 시스템](https://github.com/aisolab/flask101/wiki/06--2.-%EA%B4%80%EA%B3%84%ED%98%95-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%8B%9C%EC%8A%A4%ED%85%9C-VS-%EB%B9%84%EA%B4%80%EA%B3%84%ED%98%95-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%8B%9C%EC%8A%A4%ED%85%9C)
3. [SQL](https://github.com/aisolab/flask101/wiki/06-3.-SQL)
4. 데이터베이스 설치하기
5. [API에 데이터베이스 연결하기](https://github.com/aisolab/flask101/wiki/06-5.-API%EC%97%90-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0)
6. [SQLAlchemy를 사용하여 API와 데이터베이스 연결하기](https://github.com/aisolab/flask101/wiki/06-6.-SQLAlchemy%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-API%EC%99%80-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0)
### 07. 인증
### 08. unit test
### 09. AWS에 배포하기
### 10. API 아키텍쳐
### 11. 파일 업로드 엔드포인트
### 12. 더 좋은 백엔드 개발자가 되기위해 다음으로 배워보면 좋은 주제들
