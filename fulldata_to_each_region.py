import pandas as pd
from functools import partial
from pyproj import Transformer


pd.set_option('display.max_rows', None)  # 모든 행 표시
pd.set_option('display.max_columns', None)  # 모든 열 표시
pd.set_option('display.width', None)  # 줄 바꿈 제한 해제

df_restaurant = pd.read_csv("fulldata_restaurant.csv", encoding='cp949', low_memory=False, index_col=0)

df_restaurant = df_restaurant[['사업장명', '영업상태명', '소재지전체주소', '좌표정보(x)', '좌표정보(y)', '위생업태명']]

df_restaurant['좌표정보(y)'] = df_restaurant['좌표정보(y)'].str.replace('한식', '0')

df_restaurant['소재지전체주소'] = df_restaurant['소재지전체주소'].fillna('없음')
df_restaurant['사업장명'] = df_restaurant['사업장명'].str.replace('/', '&')
df_restaurant['사업장명'] = df_restaurant['사업장명'].str.replace('(주)', '', regex=True)

df_restaurant['좌표정보(x)'] = df_restaurant['좌표정보(x)'].astype(str)
df_restaurant['좌표정보(y)'] = df_restaurant['좌표정보(y)'].astype(str)

# 복정 있는 식당
bokjeong_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('경기도 성남시 수정구 복정')]
bokjeong_restaurant = bokjeong_restaurant[bokjeong_restaurant['영업상태명'].str.startswith('영업/정상')]
bokjeong_restaurant.to_csv("concat_restaurant/bokjeong_restaurant.csv")

# 태평 있는 식당
taepyeong_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('경기도 성남시 수정구 태평')]
taepyeong_restaurant = taepyeong_restaurant[taepyeong_restaurant['영업상태명'].str.startswith('영업/정상')]
taepyeong_restaurant.to_csv("concat_restaurant/taepyeong_restaurant.csv")

# 서울에 있는 식당
# seoul_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('서울')]
# seoul_restaurant = seoul_restaurant[seoul_restaurant['영업상태명'].str.startswith('영업/정상')]
# seoul_restaurant.to_csv("concat_restaurant/seoul_restaurant.csv")
#
# # 경기도에 있는 식당
# gyeonggi_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('경기')]
# gyeonggi_restaurant = gyeonggi_restaurant[gyeonggi_restaurant['영업상태명'].str.startswith('영업/정상')]
# gyeonggi_restaurant.to_csv("concat_restaurant/gyeonggi_restaurant.csv")
#
# # 강원도에 있는 식당
# gangwon_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('강원')]
# gangwon_restaurant = gangwon_restaurant[gangwon_restaurant['영업상태명'].str.startswith('영업/정상')]
# gangwon_restaurant.to_csv("concat_restaurant/gangwon_restaurant.csv")
#
# # 경상도에 있는 식당
# gyeongsang_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('경상')]
# gyeongsang_restaurant = gyeongsang_restaurant[gyeongsang_restaurant['영업상태명'].str.startswith('영업/정상')]
# gyeongsang_restaurant.to_csv("concat_restaurant/gyeongsang_restaurant.csv")
#
# # 전라도에 있는 식당
# jeolla_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('전라')]
# jeolla_restaurant = jeolla_restaurant[jeolla_restaurant['영업상태명'].str.startswith('영업/정상')]
# jeolla_restaurant.to_csv("concat_restaurant/jeolla_restaurant.csv")
#
# # 제주도에 있는 식당
# jeju_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('제주')]
# jeju_restaurant = jeju_restaurant[jeju_restaurant['영업상태명'].str.startswith('영업/정상')]
# jeju_restaurant.to_csv("concat_restaurant/jeju_restaurant.csv")
#
# # 충청도에 있는 식당
# chungcheong_restaurant = df_restaurant[df_restaurant['소재지전체주소'].str.startswith('충청')]
# chungcheong_restaurant = chungcheong_restaurant[chungcheong_restaurant['영업상태명'].str.startswith('영업/정상')]
# chungcheong_restaurant.to_csv("concat_restaurant/chungcheong_restaurant.csv")
