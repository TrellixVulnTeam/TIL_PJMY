# pjt 디버깅

1. 가상환경, requirements.txt 다운로드

2. migrate

3. 로드 데이터



![image-20220508173601292](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220508173601292.png)



🔴 유저 팔로우 기능 (뷰 고치고, 템플릿 script )

## accounts/views.py/ follow

4. 유저팔로우기능 (뷰 고치고, )

![image-20220508173902065](pjt 디버깅 정리.assets/image-20220508173902065.png)

![image-20220508173846863](pjt 디버깅 정리.assets/image-20220508173846863.png)

![image-20220508174154105](pjt 디버깅 정리.assets/image-20220508174154105.png)

![image-20220508174434427](pjt 디버깅 정리.assets/image-20220508174434427.png)

날 팔로잉하는 사람 수 / 내가 팔로우하는 사람 수

---

5. html 고치기

![image-20220508174747115](pjt 디버깅 정리.assets/image-20220508174747115.png)

* script 넣기

![image-20220508175128533](pjt 디버깅 정리.assets/image-20220508175128533.png)





![image-20220508175214741](pjt 디버깅 정리.assets/image-20220508175214741.png)

form 지우고

![image-20220508175241871](pjt 디버깅 정리.assets/image-20220508175241871.png)

 

![image-20220508175533912](pjt 디버깅 정리.assets/image-20220508175533912.png)

* 이제 스크립트를 짤거임

form을 처리함(여기서 비동기처리를 하니깐)

![image-20220508175815063](pjt 디버깅 정리.assets/image-20220508175815063.png)



target > dataset > userId (2번 = test값이 들어온다.)

![image-20220508175839163](pjt 디버깅 정리.assets/image-20220508175839163.png)

axios

![image-20220508180048858](pjt 디버깅 정리.assets/image-20220508180048858.png)



.then 으로 안에 내용을 바꿔줌

![image-20220508180128460](pjt 디버깅 정리.assets/image-20220508180128460.png)

로 찍어줌

![image-20220508181645102](pjt 디버깅 정리.assets/image-20220508181645102.png)

toggle, add, remove

![image-20220508181727459](pjt 디버깅 정리.assets/image-20220508181727459.png)

![image-20220508181850506](pjt 디버깅 정리.assets/image-20220508181850506.png)

---

![image-20220508182103366](pjt 디버깅 정리.assets/image-20220508182103366.png)





## 2. 좋아요

`views`

![image-20220508184358590](pjt 디버깅 정리.assets/image-20220508184358590.png)







`templates`

![image-20220508183206463](pjt 디버깅 정리.assets/image-20220508183206463.png)

![image-20220508183233925](pjt 디버깅 정리.assets/image-20220508183233925.png)



* axios

![image-20220509023548501](pjt 디버깅 정리.assets/image-20220509023548501.png)



![image-20220508183711101](pjt 디버깅 정리.assets/image-20220508183711101.png)

![image-20220508184145185](pjt 디버깅 정리.assets/image-20220508184145185.png)

![image-20220508184336287](pjt 디버깅 정리.assets/image-20220508184336287.png)



---

하트 클래스

![image-20220508184542609](pjt 디버깅 정리.assets/image-20220508184542609.png)

---

![image-20220508184729833](pjt 디버깅 정리.assets/image-20220508184729833.png)

![image-20220508184733622](pjt 디버깅 정리.assets/image-20220508184733622.png)

![image-20220508184802712](pjt 디버깅 정리.assets/image-20220508184802712.png)

60자이내





![image-20220508184829189](pjt 디버깅 정리.assets/image-20220508184829189.png)



![image-20220508184834698](pjt 디버깅 정리.assets/image-20220508184834698.png)

