## Docker-compose
> docker-compose를 통한 app 실행

[Django naming convention](https://stackoverflow.com/questions/3098681/is-there-a-naming-convention-for-django-apps)

1. 이미 django PJT를 진행 중 일때(우리의 경우)
```python
docker-compose up
```

2. startproject 할 때
  ```python
  docker-compose run web django-admin startproject testapp .
  ```
