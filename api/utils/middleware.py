white_list = ['/login', '/docs', ]

# async def auth_middleware(request: Request, call_next):
#     for item in white_list:
#         if item in request.url.path:
#             return await call_next(request)
#
#     auth_header = request.headers.get('Authorization')
#     auth_token = (auth_header or 'Bearer ').split('Bearer ')[-1]
#     if not auth_token:
#         return Unauthorized
#
#     # get last token
#     try:
#         user_token = get_user_token_by_token(db_session, auth_token)
#     except Exception as e:
#         print(e)
#         return Unauthorized
#
#     if not user_token or user_token.is_expired:
#         return Unauthorized
#
#     user = user_token.user
#
#     request.state.user = user
#     response = await call_next(request)
#     return response

# async def
