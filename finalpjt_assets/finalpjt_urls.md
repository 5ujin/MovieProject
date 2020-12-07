- accounts

  회원가입(POST) : `http://127.0.0.1:8000/accounts/signup/`

  토큰발급(POST) : `http://127.0.0.1:8000/accounts/api-token-auth/`

  프로필(GET - 조회, POST - follow) : `http://127.0.0.1:8000/accounts/<username>/`

- community

  리뷰리스트및 생성(GET - 조회, POST - 생성) :` http://127.0.0.1:8000/community/`

  리뷰상세 및 좋아요(GET - 조회, POST - 좋아요, PUT - 수정, DELETE - 삭제):` http://127.0.0.1:8000/community/<int:review_pk>/`

  댓글 생성(POST) : `http://127.0.0.1:8000/coummunity/<int:review_pk>/comments/`

  댓글 삭제(DELETE) : `http://127.0.0.1:8000/coummunity/comments/<int:comment_pk>/`

- movie

  영화목록(GET) : `http://127.0.0.1:8000/movie/`

  영화 상세페이지 및 좋아요(GET - 조회, POST - 좋아요) : `http://127.0.0.1:8000/movie/<int:movie_pk>/`

