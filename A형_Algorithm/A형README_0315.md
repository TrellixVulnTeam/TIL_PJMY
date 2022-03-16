# Queue


| Title           | Directory         | ���  |
| --------------- | ----------------- | ----- |
| 5097_ȸ��       | `5097_ȸ��`       | learn |
| 5102_����ǰŸ� | `5102_����ǰŸ�` | learn |
| 5105_�̷��ǰŸ� | `5105_�̷��ǰŸ�` | learn |
| 5099_���ڱ���   | `5099_���ڱ���`   | learn |
| 1226_�̷�1      | `1226_�̷�1`      | HW    |

## [Learn Course](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg)



## [HomeWork - 1226 �̷�1](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE&problemTitle=%EB%AF%B8%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)



## Queue : ���Լ���

* front = rear ��� ť�� ����ִٰ� �Ǵ��� �� ����
* ť�� �⺻ ���� ����

![image-20220315092254178](A%ED%98%95README_0315.assets/image-20220315092254178.png)

![image-20220315092344768](A%ED%98%95README_0315.assets/image-20220315092344768.png)

* ť�� ����

![image-20220315092232511](A%ED%98%95README_0315.assets/image-20220315092232511.png)





### ���� ť

![image-20220315092830299](A%ED%98%95README_0315.assets/image-20220315092830299.png)

![image-20220315092912206](../Django/image-20220315092912206.png)

![image-20220315093043380](A%ED%98%95README_0315.assets/image-20220315093043380.png)

![image-20220315093131092](A%ED%98%95README_0315.assets/image-20220315093131092.png)

![image-20220315093212228](A%ED%98%95README_0315.assets/image-20220315093212228.png)

* Qpeek() : ���� �տ� �ִ� ���Ҹ� �˻��Ͽ� ��ȯ
  * front+1�� �ִ� ���� ��ȯ
  * ������ ���� front�� ���� ������� �ʾƾ� �Ѵ�.

![image-20220315093328940](A%ED%98%95README_0315.assets/image-20220315093328940.png)



* ���� ť�� ������
  * ����Ʈ�� ũ�⸦ �������� �ٲ��� �ʰ� �����ϸ� ����� ť�� ũ�⸸ŭ�� �̸� Ȯ���ؾ� �ϴµ� �޸��� ���� �߻��� �� ����

![image-20220315093656499](A%ED%98%95README_0315.assets/image-20220315093656499.png)

![image-20220315093731889](A%ED%98%95README_0315.assets/image-20220315093731889.png)





### ����ť

![image-20220315093759463](A%ED%98%95README_0315.assets/image-20220315093759463.png)

![image-20220315093852635](A%ED%98%95README_0315.assets/image-20220315093852635.png)

![image-20220315093904699](A%ED%98%95README_0315.assets/image-20220315093904699.png)

* ����ť�� �⺻ ���� ����

![image-20220315094726754](A%ED%98%95README_0315.assets/image-20220315094726754.png)

![image-20220315095255759](A%ED%98%95README_0315.assets/image-20220315095255759.png)

* ����
  * ũ�� n�� 1���� ����Ʈ ���� �� front, rear = 0���� �ʱ�ȭ
  * 

![image-20220315095353053](A%ED%98%95README_0315.assets/image-20220315095353053.png)

![image-20220315095706664](A%ED%98%95README_0315.assets/image-20220315095706664.png)

![image-20220315100711544](A%ED%98%95README_0315.assets/image-20220315100711544.png)

![image-20220315101102618](A%ED%98%95README_0315.assets/image-20220315101102618.png)

![image-20220315101116456](A%ED%98%95README_0315.assets/image-20220315101116456.png)



* ���̽��� ����Ʈ Ư���� ����� ť

![image-20220315101145717](A%ED%98%95README_0315.assets/image-20220315101145717.png)

![image-20220315102409594](A%ED%98%95README_0315.assets/image-20220315102409594.png)





### ���� ť = ���� ����Ʈ

![image-20220315102743246](A%ED%98%95README_0315.assets/image-20220315102743246.png)

![image-20220315103012532](A%ED%98%95README_0315.assets/image-20220315103012532.png)

![image-20220315103027934](A%ED%98%95README_0315.assets/image-20220315103027934.png)

![image-20220315103112817](A%ED%98%95README_0315.assets/image-20220315103112817.png)



### BFS : �ʺ� �켱 Ž��

![image-20220315110049381](A%ED%98%95README_0315.assets/image-20220315110049381.png)

* Ž�� ���� : A B C D E F G H I

![image-20220315110124743](A%ED%98%95README_0315.assets/image-20220315110124743.png)

![image-20220315110156469](A%ED%98%95README_0315.assets/image-20220315110156469.png)



* visited ����Ʈ, queue

![image-20220315111603612](A%ED%98%95README_0315.assets/image-20220315111603612.png)

5097. [���̽� S/W �����ذ� �⺻] 6���� - ȸ��

5105. [���̽� S/W �����ذ� �⺻] 6���� - �̷��� �Ÿ�



## ����

A�� ���� :���Ƕ�� ġ�� ����Ѱ� ���� ����



![image-20220315130239742](A%ED%98%95README_0315.assets/image-20220315130239742.png)

���� 

https://www.acmicpc.net/workbook/view/1152

![image-20220315130929003](A%ED%98%95README_0315.assets/image-20220315130929003.png)



ť