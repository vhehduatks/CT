"""
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
자연수 N이 주어졌을 때, g(N)을 구해보자.
"""

N=int(input())
ret=0

# N/i 가 N까지의 약수의 갯수인 이유 : i를 약수로 가진다 -> i의 배수이다 -> i를 k번 더한 i의 배수가 N보다 작다면 N 까지의 약수 안에 약수 i는 k번 들어있다는 뜻이므로
# N/i 는 1부터 N까지의 약수를 구할 경우에 나타나는 약수 i 의 갯수이다.
for i in range(1,N+1):
	ret+=(N//i)*i

print(ret)