# -*- conding: utf-8 -*-
import json
from pprint import pprint
response = json.loads('{"header":{"resultCode":200,"resultMessage":"SUCCESS"},"data":' \
           '{"totalCount":44020,"merchants":[{"totalCount":44020,"seq":1279364,"regDate":1505303413933,' \
           '"simpleNm":"#(샵)SHARP모텔","zipCd":"10462","addr":"경기 고양시 덕양구 호국로801번길 5","telephone":"031-' \
           '962-7300","bizType":"1020","bizTypeNm":"숙박업","bizTypeDetail":"여관/기타숙박업","salesCd":"8","latitude":' \
           '37.657439222,"longitude":126.8367908821,"distance":null},{"totalCount":44020,"seq":3299814,"regDate":152840885029' \
           '3,"simpleNm":"#703","zipCd":"10464","addr":"경기 고양시 덕양구 고양대로 1371","telephone":"031-963-0070","bizTy' \
           'pe":"8001","bizTypeNm":"일반휴게음식","bizTypeDetail":"일반한식","salesCd":"8","latitude":37.6547449362,"longit' \
           'ude":126.8365135782,"distance":null},{"totalCount":44020,"seq":3796197,"regDate":1561068056560,"simpleNm":"#' \
           'EEFF0C","zipCd":"10374","addr":"경기 고양시 일산서구 강선로 167","telephone":"010-****-7562","bizType":"8006","' \
           'bizTypeNm":"일반휴게음식","bizTypeDetail":"서양음식","salesCd":"8","latitude":37.6784068676,"longitude":126.768' \
           '990036,"distance":null},{"totalCount":44020,"seq":300715,"regDate":1505300325690,"simpleNm":"#끌림헤어(hair)",' \
           '"zipCd":"10465","addr":"경기 고양시 덕양구 충장로475번길 14-5","telephone":"010-****-2496","bizType":"7102","biz' \
           'TypeNm":"보건위생","bizTypeDetail":"미용원","salesCd":"8","latitude":37.0,"longitude":126.0,"distance":null},{"t' \
           'otalCount":44020,"seq":3190469,"regDate":1521583253196,"simpleNm":"(BG)공조시스템","zipCd":"10551","addr":"경기' \
           ' 고양시 덕양구 도래울안길 22-1","telephone":"031-000-0000","bizType":"9199","bizTypeNm":"용역 서비스","bizTypeDet' \
           'ail":"기타용역서비스","salesCd":"8","latitude":37.6298062846,"longitude":126.8725029612,"distance":null},{"tota' \
           'lCount":44020,"seq":1932560,"regDate":1505305248917,"simpleNm":"(GoGo)고고비어","zipCd":"10222","addr":"경기 고양' \
           '시 일산서구 대화로 136","telephone":"031-915-5392","bizType":"8001","bizTypeNm":"일반휴게음식","bizTypeDetail":"일반한' \
           '식","salesCd":"8","latitude":37.6702710421,"longitude":126.7350458992,"distance":null},{"totalCount":44020,"seq":412801' \
           '5,"regDate":1584568862999,"simpleNm":"(K)아이스크림 할인점(탄현2호점)","zipCd":"10343","addr":"경기 고양시 일산서구 산현로 ' \
           '15","telephone":"031-921-0344","bizType":"8399","bizTypeNm":"음료식품","bizTypeDetail":"기타음료식품","salesCd":"S","la' \
           'titude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3977815,"regDate":1573768856162,"simpleNm":"' \
           '(KHU)경희대태권도장","zipCd":"10486","addr":"경기 고양시 덕양구 중앙로 440","telephone":"031-979-7667","bizType":"5104","' \
           'bizTypeNm":"학원","bizTypeDetail":"예•체능계학원 ","salesCd":"8","latitude":null,"longitude":null,"distance":null},{"' \
           '":44020,"seq":3929040,"regDate":1570572096199,"simpleNm":"(THE)뚜벅이족발","zipCd":"10250","addr":"경기 고양시 일산동구 고봉' \
           '로 626","telephone":"031-975-2007","bizType":"8001","bizTypeNm":"일반휴게음식","bizTypeDetail":"일반한식","salesCd":"8","lat' \
           'itude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3527737,"regDate":1543960861388,"simpleNm":"(W)모텔"' \
           ',"zipCd":"10272","addr":"경기 고양시 덕양구 혜음로 78","telephone":"031-962-2480","bizType":"1020","bizTypeNm":"숙박업","bizT' \
           'ypeDetail":"여관/기타숙박업","salesCd":"8","latitude":37.7074088477,"longitude":126.9024754558,"distance":null},{"totalCoun' \
           't":44020,"seq":4094213,"regDate":1582149657614,"simpleNm":"(YBM)리딩클럽","zipCd":"10508","addr":"경기 고양시 덕양구 능곡로13' \
           '번길 16","telephone":"010-****-3802","bizType":"5199","bizTypeNm":"학원","bizTypeDetail":"기타 교육기관","salesCd":"S","lati' \
           'tude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3526379,"regDate":1543874453896,"simpleNm":"(e)해법' \
           '수학 탄현 에듀포레점","zipCd":"10248","addr":"경기 고양시 일산서구 탄현로 136","telephone":"010-****-0588","bizType":"5199","biz' \
           'TypeNm":"학원","bizTypeDetail":"기타 교육기관","salesCd":"8","latitude":37.7039828054,"longitude":126.7677984046,"distance"' \
           ':null},{"totalCount":44020,"seq":3216300,"regDate":1522965661540,"simpleNm":"(고양) 하늘소리 요양원","zipCd":"10279","addr":' \
           '"경기 고양시 덕양구 동헌로 319-25","telephone":"031-969-1693","bizType":"7099","bizTypeNm":"기타의료기관","bizTypeDetail":"기타' \
           '의료기관 및 기타의료기기","salesCd":"8","latitude":37.7112357384,"longitude":126.8900861193,"distance":null},{"totalCount":44' \
           '020,"seq":3052794,"regDate":1512597677496,"simpleNm":"(고양)늘기쁜주야간보호센터","zipCd":"10462","addr":"경기 고양시 덕양구 마상' \
           '로140번길 48","telephone":"031-964-6888","bizType":"7099","bizTypeNm":"기타의료기관","bizTypeDetail":"기타의료기관 및 기타의료기' \
           '기","salesCd":"8","latitude":37.65771769,"longitude":126.8362009632,"distance":null},{"totalCount":44020,"seq":2506947,"r' \
           'egDate":1505307089731,"simpleNm":"(고양)서울요양원","zipCd":"10267","addr":"경기 고양시 덕양구 보광로128번길 16-2","telephone' \
           '":"031-964-3020","bizType":"7099","bizTypeNm":"기타의료기관","bizTypeDetail":"기타의료기관 및 기타의료기기","salesCd":"8","la' \
           'titude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":3887071,"regDate":1567202459549,"simpleNm":"(고양' \
           ')아이미래로 일산","zipCd":"10497","addr":"경기 고양시 덕양구 화중로104번길 28","telephone":"031-921-5992","bizType":"7199","bi' \
           'zTypeNm":"보건위생","bizTypeDetail":"기타대인서비스","salesCd":"8","latitude":37.0,"longitude":126.0,"distance":null},{"tot' \
           'alCount":44020,"seq":447022,"regDate":1505300807916,"simpleNm":"(구)양지마을","zipCd":"10492","addr":"경기 고양시 덕양구 행신' \
           '동","telephone":"031-974-0778","bizType":"8001","bizTypeNm":"일반휴게음식","bizTypeDetail":"일반한식","salesCd":"8","latitud' \
           'e":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":1942484,"regDate":1505305280537,"simpleNm":"(금)에스테틱",' \
           '"zipCd":"10486","addr":"경기 고양시 덕양구 중앙로 442","telephone":"031-818-8082","bizType":"9398","bizTypeNm":"회원제형태","bizT' \
           'ypeDetail":"기타4","salesCd":"8","latitude":37.6181963759,"longitude":126.8458942405,"distance":null},{"totalCount":44020,"seq' \
           '":3880554,"regDate":1566856869408,"simpleNm":"(달)Moon","zipCd":"10208","addr":"경기 고양시 일산서구 가좌로 54","telephone":"010-' \
           '****-0132","bizType":"4201","bizTypeNm":"의류","bizTypeDetail":"정장","salesCd":"8","latitude":37.0,"longitude":126.0,"distance' \
           '":null},{"totalCount":44020,"seq":2971129,"regDate":1506636279863,"simpleNm":"(문지향)","zipCd":"10417","addr":"경기 고양시 일산' \
           '동구 강촌로 191","telephone":"031-813-5261","bizType":"9130","bizTypeNm":"용역 서비스","bizTypeDetail":"사무서비스","salesCd":"8","latit' \
           'ude":37.6559751793,"longitude":126.7942636552,"distance":null},{"totalCount":44020,"seq":2565742,"regDate":1505307280714,"simpleNm":"' \
           '(본점)리빙센스미용실","zipCd":"10526","addr":"경기 고양시 덕양구 충경로 44","telephone":"031-978-1888","bizType":"7102","bizTypeNm":"보건' \
           '위생","bizTypeDetail":"미용원","salesCd":"8","latitude":37.6151893291,"longitude":126.8344271125,"distance":null},{"totalCount":44020,' \
           '"seq":4072676,"regDate":1580767256854,"simpleNm":"(사) 나눔해요운동본부","zipCd":"10440","addr":"경기 고양시 덕양구 행주로17번길 42-7","te' \
           'lephone":"070-8806-4987","bizType":"9110","bizTypeNm":"용역 서비스","bizTypeDetail":"가례서비스업","salesCd":"S","latitude":null,"longi' \
           'tude":null,"distance":null},{"totalCount":44020,"seq":2217245,"regDate":1505306146278,"simpleNm":"(사)감돌역사문화연구회","zipCd":"1036' \
           '8","addr":"경기 고양시 일산서구 일산로 662","telephone":"070-7509-6435","bizType":"5199","bizTypeNm":"학원","bizTypeDetail":"기타 교육기관' \
           '","salesCd":"8","latitude":37.6829297722,"longitude":126.7557688286,"distance":null},{"totalCount":44020,"seq":1220848,"regDate":1505' \
           '303260084,"simpleNm":"(사)경기도북부자동차정비사업조합","zipCd":"10253","addr":"경기 고양시 일산동구 장진천길 66-4","telephone":"031-979-50' \
           '70","bizType":"9910","bizTypeNm":"기타","bizTypeDetail":"비영리/대상","salesCd":"8","latitude":37.7131791609,"longitude":126.811262468' \
           '4,"distance":null},{"totalCount":44020,"seq":1487550,"regDate":1505303959992,"simpleNm":"(사)국제청소년221(고양지부)","zipCd":"10406","' \
           'addr":"경기 고양시 일산동구 일산로380번길 25-10","telephone":"031-902-7895","bizType":"9910","bizTypeNm":"기타","bizTypeDetail":"비영리/대' \
           '상","salesCd":"8","latitude":37.6700987368,"longitude":126.782379532,"distance":null},{"totalCount":44020,"seq":3021384,"regDate":151' \
           '0610471237,"simpleNm":"(사)민족토속문화유산 샤먼스테이 명신굿당","zipCd":"10277","addr":"경기 고양시 덕양구 선유길 161-113","telephone":"03' \
           '1-000-0000","bizType":"7199","bizTypeNm":"보건위생","bizTypeDetail":"기타대인서비스","salesCd":"K","latitude":37.0,"longitude":126.0,"d' \
           'istance":null},{"totalCount":44020,"seq":2716626,"regDate":1505307770825,"simpleNm":"(사)사랑채유료노인전문요양원","zipCd":"10566","addr' \
           '":"경기 고양시 덕양구 통일로 413-19","telephone":"02-381-0500","bizType":"7099","bizTypeNm":"기타의료기관","bizTypeDetail":"기타의료기관 및' \
           ' 기타의료기기","salesCd":"8","latitude":37.6719932116,"longitude":126.8843987799,"distance":null},{"totalCount":44020,"seq":818161,"re' \
           'gDate":1505302033523,"simpleNm":"(사)일산국제문화예능포럼일산교육문화원","zipCd":"10380","addr":"경기 고양시 일산서구 강성로 239","telephone' \
           '":"031-915-1494","bizType":"2299","bizTypeNm":"문화.취미","bizTypeDetail":"문화취미기타","salesCd":"8","latitude":37.675629383,"longitu' \
           'de":126.7502953853,"distance":null},{"totalCount":44020,"seq":4197318,"regDate":1589839262402,"simpleNm":"(사)한국농업경영인고양시","zi' \
           'pCd":"10400","addr":"경기 고양시 일산동구 호수로 595","telephone":"031-901-1355","bizType":"2230","bizTypeNm":"문화.취미","bizTypeDetail"' \
           ':"화원","salesCd":"S","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":1468235,"regDate":1505303910144,"si' \
           'mpleNm":"(사)한국신체장애인복지회인쇄사업장","zipCd":"08505","addr":"서울 금천구 가산디지털2로 107","telephone":"02-6401-8891","bizType":"5' \
           '010","bizTypeNm":"서적문구","bizTypeDetail":"출판 및 인쇄물","salesCd":"1","latitude":null,"longitude":null,"distance":null},{"totalCou' \
           'nt":44020,"seq":919825,"regDate":1505302346978,"simpleNm":"(사)한국연설연구협회연수원","zipCd":"10500","addr":"경기 고양시 덕양구 화신로26' \
           '0번길 37","telephone":"031-971-0498","bizType":"9910","bizTypeNm":"기타","bizTypeDetail":"비영리/대상","salesCd":"8","latitude":37.6324' \
           '131471,"longitude":126.8324849994,"distance":null},{"totalCount":44020,"seq":1240373,"regDate":1505303310841,"simpleNm":"(사)한국외식업' \
           '중앙회고양시일산구지부","zipCd":"10414","addr":"경기 고양시 일산동구 장백로 184","telephone":"031-906-1661","bizType":"9911","bizTypeNm":"' \
           '기타","bizTypeDetail":"비영리/비대상","salesCd":"J","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":275676' \
           '8,"regDate":1505307902034,"simpleNm":"(사)한국원예문화협회 뜰안에사업단","zipCd":"10299","addr":"경기 고양시 일산동구 식사동","telephone":"' \
           '031-903-1245","bizType":"2230","bizTypeNm":"문화.취미","bizTypeDetail":"화원","salesCd":"8","latitude":37.6759638322,"longitude":126.8' \
           '190663129,"distance":null},{"totalCount":44020,"seq":2560354,"regDate":1505307262649,"simpleNm":"(사)한국정보교육문화협회","zipCd":"102' \
           '23","addr":"경기 고양시 일산서구 중앙로 1601","telephone":"031-911-7115","bizType":"9305","bizTypeNm":"회원제형태","bizTypeDetail":"학원"' \
           ',"salesCd":"8","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":608110,"regDate":1505301340083,"simpleNm":"(' \
           '사)한국정보교육문화협회덕양지부","zipCd":"10492","addr":"경기 고양시 덕양구 중앙로472번길 65","telephone":"031-974-9484","bizType":"7199","b' \
           'izTypeNm":"보건위생","bizTypeDetail":"기타대인서비스","salesCd":"8","latitude":37.6219415643,"longitude":126.8437568454,"distance":null}' \
           ',{"totalCount":44020,"seq":823824,"regDate":1505302049180,"simpleNm":"(사단)한국항공운항학회","zipCd":"10537","addr":"경기 고양시 덕양구 ' \
           '화전동","telephone":"02-300-0174","bizType":"9911","bizTypeNm":"기타","bizTypeDetail":"비영리/비대상","salesCd":"8","latitude":null,"lo' \
           'ngitude":null,"distance":null},{"totalCount":44020,"seq":4000154,"regDate":1575324060828,"simpleNm":"(신)헝그리웍","zipCd":"10208","ad' \
           'dr":"경기 고양시 일산서구 가좌로 34-4","telephone":"031-923-5282","bizType":"8005","bizTypeNm":"일반휴게음식","bizTypeDetail":"중국식","sa' \
           'lesCd":"8","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":900961,"regDate":1505302284538,"simpleNm":"(원' \
           '희)발렌시아","zipCd":"10500","addr":"경기 고양시 덕양구 화정로 52","telephone":"031-972-7077","bizType":"4201","bizTypeNm":"의류","bizTyp' \
           'eDetail":"정장","salesCd":"8","latitude":37.6342765107,"longitude":126.8313478342,"distance":null},{"totalCount":44020,"seq":2355756,' \
           '"regDate":1505306597693,"simpleNm":"(유)골든에이스","zipCd":"10366","addr":"경기 고양시 일산서구 중앙로 1371","telephone":"02-2077-1288",' \
           '"bizType":"4201","bizTypeNm":"의류","bizTypeDetail":"정장","salesCd":"8","latitude":37.6666253161,"longitude":126.7660121649,"distance' \
           '":null},{"totalCount":44020,"seq":1804961,"regDate":1505304831292,"simpleNm":"(유)웰드원(Weldwone Ltd)","zipCd":"10540","addr":"경기 고' \
           '양시 덕양구 항공대학로 76","telephone":"02-3159-0454","bizType":"9901","bizTypeNm":"기타","bizTypeDetail":"기계공구","salesCd":"8","lati' \
           'tude":37.5991377549,"longitude":126.8651507439,"distance":null},{"totalCount":44020,"seq":2893192,"regDate":1505308352914,"simpleNm":' \
           '"(유)케이투지비에스","zipCd":"10390","addr":"경기 고양시 일산서구 한류월드로 407","telephone":"031-995-6500","bizType":"1110","bizTypeNm":' \
           '"여행","bizTypeDetail":"관광여행","salesCd":"8","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3923750,"r' \
           'egDate":1570053665429,"simpleNm":"(유)탑어드밴싱 사리현점","zipCd":"10259","addr":"경기 고양시 일산동구 성현로 488","telephone":"070-5088-' \
           '5601","bizType":"4201","bizTypeNm":"의류","bizTypeDetail":"정장","salesCd":"S","latitude":null,"longitude":null,"distance":null},{"tot' \
           'alCount":44020,"seq":2167479,"regDate":1505305984310,"simpleNm":"(유니베라) 박현숙","zipCd":"10420","addr":"경기 고양시 일산동구 강송로 1' \
           '19","telephone":"031-902-9994","bizType":"9395","bizTypeNm":"회원제형태","bizTypeDetail":"기타1","salesCd":"8","latitude":37.0,"longit' \
           'ude":126.0,"distance":null},{"totalCount":44020,"seq":549888,"regDate":1505301146179,"simpleNm":"(일산시장점)이디야커피전문점","zipCd":"' \
           '10350","addr":"경기 고양시 일산서구 원일로 69","telephone":"031-975-6765","bizType":"8006","bizTypeNm":"일반휴게음식","bizTypeDetail":"서' \
           '양음식","salesCd":"8","latitude":37.6867340708,"longitude":126.7701542811,"distance":null},{"totalCount":44020,"seq":1581900,"regDate"' \
           ':1505304206454,"simpleNm":"(재)고양국제꽃박람회","zipCd":"10400","addr":"경기 고양시 일산동구 호수로 595","telephone":"031-908-7644","bizT' \
           'ype":"2251","bizTypeNm":"문화.취미","bizTypeDetail":"티켓","salesCd":"1","latitude":null,"longitude":null,"distance":null},{"totalCoun' \
           't":44020,"seq":1662132,"regDate":1505304415774,"simpleNm":"(재)고양국제꽃박람회","zipCd":"10400","addr":"경기 고양시 일산동구 호수로 595",' \
           '"telephone":"031-908-7644","bizType":"9010","bizTypeNm":"건축자재","bizTypeDetail":"인테리어전문","salesCd":"1","latitude":null,"longit' \
           'ude":null,"distance":null},{"totalCount":44020,"seq":2362665,"regDate":1505306620335,"simpleNm":"(재)고양국제꽃박람회","zipCd":"10400",' \
           '"addr":"경기 고양시 일산동구 호수로 595","telephone":"031-908-7644","bizType":"9910","bizTypeNm":"기타","bizTypeDetail":"비영리/대상","sa' \
           'lesCd":"1","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":2603608,"regDate":1505307402845,"simpleNm":"(' \
           '재)고양국제꽃박람회","zipCd":"10400","addr":"경기 고양시 일산동구 호수로 595","telephone":"031-908-7644","bizType":"2251","bizTypeNm":"문' \
           '화.취미","bizTypeDetail":"티켓","salesCd":"1","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":1245367,"reg' \
           'Date":1505303323809,"simpleNm":"(재)아름다운가게일산마두역점","zipCd":"10414","addr":"경기 고양시 일산동구 중앙로 1160","telephone":"02-211' \
           '5-7205","bizType":"4499","bizTypeNm":"신변잡화","bizTypeDetail":"기타잡화","salesCd":"1","latitude":null,"longitude":null,"distance":nu' \
           'll},{"totalCount":44020,"seq":2813163,"regDate":1505308085475,"simpleNm":"(재)중남미문화원","zipCd":"10273","addr":"경기 고양시 덕양구 대' \
           '양로285번길 33-15","telephone":"031-962-7171","bizType":"9910","bizTypeNm":"기타","bizTypeDetail":"비영리/대상","salesCd":"A","latitude' \
           '":37.703519358,"longitude":126.8952800298,"distance":null},{"totalCount":44020,"seq":1240629,"regDate":1505303311575,"simpleNm":"(재)' \
           '한국중독연구재단 청미래","zipCd":"10450","addr":"경기 고양시 일산동구 일산로 86","telephone":"031-810-9064","bizType":"8006","bizTypeNm":"' \
           '일반휴게음식","bizTypeDetail":"서양음식","salesCd":"1","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":4025' \
           '696,"regDate":1577138458071,"simpleNm":"(주) JB","zipCd":"10558","addr":"경기 고양시 덕양구 권율대로 726","telephone":"010-****-8428","b' \
           'izType":"4499","bizTypeNm":"신변잡화","bizTypeDetail":"기타잡화","salesCd":"8","latitude":null,"longitude":null,"distance":null},{"tota' \
           'lCount":44020,"seq":4099013,"regDate":1582581644509,"simpleNm":"(주) 가인에스엠","zipCd":"10595","addr":"경기 고양시 덕양구 동송로 33","t' \
           'elephone":"031-968-0384","bizType":"3199","bizTypeNm":"전기제품","bizTypeDetail":"기타전기제품","salesCd":"K","latitude":null,"longitud' \
           'e":null,"distance":null},{"totalCount":44020,"seq":168018,"regDate":1505299885003,"simpleNm":"(주) 거원비즈니스솔루션","zipCd":"10335",' \
           '"addr":"경기 고양시 일산동구 성석로 57-3","telephone":"031-975-1235","bizType":"5202","bizTypeNm":"사무통신","bizTypeDetail":"사무용 OA기' \
           '기","salesCd":"8","latitude":37.6849637045,"longitude":126.7917110695,"distance":null},{"totalCount":44020,"seq":3484505,"regDate":15' \
           '40936855092,"simpleNm":"(주) 꽃길","zipCd":"10526","addr":"경기 고양시 덕양구 용현로 9","telephone":"010-****-9979","bizType":"2230","bi' \
           'zTypeNm":"문화.취미","bizTypeDetail":"화원","salesCd":"8","latitude":37.6135780886,"longitude":126.8354840617,"distance":null},{"total' \
           'Count":44020,"seq":3365557,"regDate":1532469652167,"simpleNm":"(주) 내셔널투어니스","zipCd":"10386","addr":"경기 고양시 일산서구 주화로 4' \
           '0","telephone":"031-1644-5895","bizType":"1110","bizTypeNm":"여행","bizTypeDetail":"관광여행","salesCd":"8","latitude":null,"longitude' \
           '":null,"distance":null},{"totalCount":44020,"seq":3610887,"regDate":1550008901249,"simpleNm":"(주) 늘푸른식자재","zipCd":"10220","addr"' \
           ':"경기 고양시 일산서구 대화로37번길 17-6","telephone":"031-000-0000","bizType":"8399","bizTypeNm":"음료식품","bizTypeDetail":"기타음료식품' \
           '","salesCd":"A","latitude":37.6658799309,"longitude":126.7257678919,"distance":null},{"totalCount":44020,"seq":428651,"regDate":15053' \
           '00747155,"simpleNm":"(주) 다즐에듀","zipCd":"10359","addr":"경기 고양시 일산동구 대산로 14","telephone":"070-8809-5525","bizType":"5050",' \
           '"bizTypeNm":"서적문구","bizTypeDetail":"완구점","salesCd":"K","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"s' \
           'eq":3311417,"regDate":1529100172654,"simpleNm":"(주) 동문 시스텍","zipCd":"10415","addr":"경기 고양시 일산동구 강송로 149","telephone":"0' \
           '31-905-0181","bizType":"5040","bizTypeNm":"서적문구","bizTypeDetail":"과학기자재","salesCd":"A","latitude":37.6520993807,"longitude":12' \
           '6.7834299616,"distance":null},{"totalCount":44020,"seq":108139,"regDate":1505299687167,"simpleNm":"(주) 로스오토웍스","zipCd":"10317","' \
           'addr":"경기 고양시 일산동구 견달산로225번길 51","telephone":"031-965-9320","bizType":"6110","bizTypeNm":"자동차정비 유지","bizTypeDetail":' \
           '"자동차정비","salesCd":"A","latitude":37.6870968281,"longitude":126.8172022252,"distance":null},{"totalCount":44020,"seq":3736536,"reg' \
           'Date":1557266467300,"simpleNm":"(주) 리너지","zipCd":"10550","addr":"경기 고양시 덕양구 삼원안길 10","telephone":"010-****-0456","bizType' \
           '":"6102","bizTypeNm":"자동차정비 유지","bizTypeDetail":"자동차부품","salesCd":"8","latitude":37.6363857646,"longitude":126.8746780456,"d' \
           'istance":null},{"totalCount":44020,"seq":3484168,"regDate":1540936854151,"simpleNm":"(주) 마이다스웰","zipCd":"10414","addr":"경기 고양' \
           '시 일산동구 중앙로 1192","telephone":"070-0000-0000","bizType":"4201","bizTypeNm":"의류","bizTypeDetail":"정장","salesCd":"8","latitude"' \
           ':37.6531602879,"longitude":126.7774662268,"distance":null},{"totalCount":44020,"seq":3812007,"regDate":1562018466996,"simpleNm":"(주)' \
           ' 모터원 고양사고수리 전문센터","zipCd":"10329","addr":"경기 고양시 일산동구 성석로 209","telephone":"031-979-4134","bizType":"6102","bizTyp' \
           'eNm":"자동차정비 유지","bizTypeDetail":"자동차부품","salesCd":"S","latitude":37.6954875036,"longitude":126.7971236609,"distance":null},{' \
           '"totalCount":44020,"seq":200620,"regDate":1505299993544,"simpleNm":"(주) 모하니","zipCd":"10313","addr":"경기 고양시 일산동구 성현로268번' \
           '길 68-85","telephone":"070-8240-2247","bizType":"2251","bizTypeNm":"문화.취미","bizTypeDetail":"티켓","salesCd":"8","latitude":37.70162' \
           '41684,"longitude":126.8084006837,"distance":null},{"totalCount":44020,"seq":3717513,"regDate":1556056851701,"simpleNm":"(주) 몽키웍스"' \
           ',"zipCd":"10431","addr":"경기 고양시 일산동구 장항로 257","telephone":"031-924-1382","bizType":"6101","bizTypeNm":"자동차정비 유지","bizT' \
           'ypeDetail":"자동차시트•타이어","salesCd":"K","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":3767318,"regD' \
           'ate":1559167377604,"simpleNm":"(주) 분다 스시히로바 일산점","zipCd":"10416","addr":"경기 고양시 일산동구 일산로 255","telephone":"031-903-' \
           '3292","bizType":"8004","bizTypeNm":"일반휴게음식","bizTypeDetail":"일식•회집","salesCd":"K","latitude":37.0,"longitude":126.0,"distance' \
           '":null},{"totalCount":44020,"seq":1038511,"regDate":1505302743355,"simpleNm":"(주) 비케이 인터내셔널","zipCd":"10449","addr":"경기 고양' \
           '시 일산동구 호수로 358-25","telephone":"070-4350-5962","bizType":"8499","bizTypeNm":"건강식품","bizTypeDetail":"기타건강식품","salesCd":"' \
           'J","latitude":37.6399409743,"longitude":126.7859583195,"distance":null},{"totalCount":44020,"seq":234913,"regDate":1505300106790,"sim' \
           'pleNm":"(주) 세운건설","zipCd":"10401","addr":"경기 고양시 일산동구 중앙로1275번길 60-31","telephone":"031-973-4020","bizType":"9199","bi' \
           'zTypeNm":"용역 서비스","bizTypeDetail":"기타용역서비스","salesCd":"8","latitude":37.6600170665,"longitude":126.7684357585,"distance":nul' \
           'l},{"totalCount":44020,"seq":3682341,"regDate":1553896860574,"simpleNm":"(주) 세운종합상사","zipCd":"10549","addr":"경기 고양시 덕양구 용' \
           '두로 10-1","telephone":"02-357-6363","bizType":"9099","bizTypeNm":"건축자재","bizTypeDetail":"기타건축자재","salesCd":"8","latitude":37.' \
           '0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":3839993,"regDate":1563832866989,"simpleNm":"(주) 센텀헬스케어","zipCd":"' \
           '10388","addr":"경기도 고양시 일산서구 대산로 145","telephone":"031-994-8765","bizType":"8499","bizTypeNm":"건강식품","bizTypeDetail":"기타' \
           '건강식품","salesCd":"8","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":586064,"regDate":1505301267884,"s' \
           'impleNm":"(주) 스마트메디칼디바이스","zipCd":"10364","addr":"경기 고양시 일산동구 고봉로 32-19","telephone":"070-7525-2100","bizType":"913' \
           '4","bizTypeNm":"용역 서비스","bizTypeDetail":"소프트웨어","salesCd":"A","latitude":37.6641850552,"longitude":126.7666886039,"distance":' \
           'null},{"totalCount":44020,"seq":4148336,"regDate":1586210453908,"simpleNm":"(주) 시스코프","zipCd":"10257","addr":"경기 고양시 일산동구 ' \
           '장진천길 30-97","telephone":"031-000-0000","bizType":"3001","bizTypeNm":"가구","bizTypeDetail":"일반가구","salesCd":"S","latitude":null' \
           ',"longitude":null,"distance":null},{"totalCount":44020,"seq":4102686,"regDate":1582754451174,"simpleNm":"(주) 신세계 환경","zipCd":"10' \
           '406","addr":"경기 고양시 일산동구 일산로394번길 5-4","telephone":"031-908-7482","bizType":"9101","bizTypeNm":"용역 서비스","bizTypeDetail' \
           '":"종합용역","salesCd":"S","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":493135,"regDate":1505300960449,"' \
           'simpleNm":"(주) 씨엠커뮤니티","zipCd":"10403","addr":"경기 고양시 일산동구 백마로 195","telephone":"031-902-1671","bizType":"9101","bizTyp' \
           'eNm":"용역 서비스","bizTypeDetail":"종합용역","salesCd":"J","latitude":37.6547150419,"longitude":126.7707981942,"distance":null},{"total' \
           'Count":44020,"seq":186965,"regDate":1505299947962,"simpleNm":"(주) 아이엘인터내셔날","zipCd":"10257","addr":"경기 고양시 일산동구 문봉길 7' \
           '8","telephone":"031-977-8002","bizType":"4201","bizTypeNm":"의류","bizTypeDetail":"정장","salesCd":"8","latitude":37.7058516901,"longit' \
           'ude":126.8152049698,"distance":null},{"totalCount":44020,"seq":3529667,"regDate":1544047255550,"simpleNm":"(주) 아이테크놀러지","zipCd":' \
           '"10257","addr":"경기 고양시 일산동구 문봉길 54-7","telephone":"031-977-7881","bizType":"5299","bizTypeNm":"사무통신","bizTypeDetail":"기타' \
           ' 사무용품","salesCd":"J","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":2705687,"regDate":1505307734294,"' \
           'simpleNm":"(주) 와이케이동그라미 일산화정지점","zipCd":"10500","addr":"경기 고양시 덕양구 화중로 72","telephone":"031-819-1000","bizType":"7' \
           '044","bizTypeNm":"기타의료기관","bizTypeDetail":"산후조리원","salesCd":"1","latitude":37.0,"longitude":126.0,"distance":null},{"totalCou' \
           'nt":44020,"seq":1445648,"regDate":1505303852358,"simpleNm":"(주) 우리전자기술","zipCd":"10526","addr":"경기 고양시 덕양구 용현로 3","telep' \
           'hone":"031-926-3309","bizType":"3199","bizTypeNm":"전기제품","bizTypeDetail":"기타전기제품","salesCd":"A","latitude":37.6130016272,"long' \
           'itude":126.8355986127,"distance":null},{"totalCount":44020,"seq":3381924,"regDate":1533592850059,"simpleNm":"(주) 인피루트 필더블랭크 지점",' \
           '"zipCd":"10509","addr":"경기 고양시 덕양구 토당로 35","telephone":"031-503-8488","bizType":"8006","bizTypeNm":"일반휴게음식","bizTypeDetail":' \
           '"서양음식","salesCd":"8","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3984067,"regDate":1574200858810,"si' \
           'mpleNm":"(주) 일산애니포스","zipCd":"10387","addr":"경기 고양시 일산서구 중앙로 1449","telephone":"031-917-5753","bizType":"5104","bizTypeNm' \
           '":"학원","bizTypeDetail":"예•체능계학원 ","salesCd":"8","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":560658' \
           ',"regDate":1505301182330,"simpleNm":"(주) 자연과 사람들","zipCd":"10296","addr":"경기 고양시 덕양구 마상로57번길 87-70","telephone":"031-528-3' \
           '580","bizType":"8399","bizTypeNm":"음료식품","bizTypeDetail":"기타음료식품","salesCd":"8","latitude":37.6684635846,"longitude":126.8343407' \
           '774,"distance":null},{"totalCount":44020,"seq":2938950,"regDate":1505308504871,"simpleNm":"(주) 케이우드빌","zipCd":"10202","addr":"경기 ' \
           '고양시 일산서구 송산로 164","telephone":"031-921-6012","bizType":"9099","bizTypeNm":"건축자재","bizTypeDetail":"기타건축자재","salesCd":"J' \
           '","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":2071749,"regDate":1505305679631,"simpleNm":"(주) 쿱스토' \
           '어 경기 마두점","zipCd":"10416","addr":"경기 고양시 일산동구 일산로 217","telephone":"031-919-7600","bizType":"4020","bizTypeNm":"유통업 ' \
           '영리","bizTypeDetail":"슈퍼마켓","salesCd":"1","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3754843,"reg' \
           'Date":1558389664152,"simpleNm":"(주) 크립텍스","zipCd":"10594","addr":"경기 고양시 덕양구 통일로 140","telephone":"070-4837-4951","bizTy' \
           'pe":"9210","bizTypeNm":"수리서비스","bizTypeDetail":"세탁소","salesCd":"K","latitude":37.0,"longitude":126.0,"distance":null},{"total' \
           'Count":44020,"seq":3758803,"regDate":1558562459779,"simpleNm":"(주) 크립텍스","zipCd":"10594","addr":"경기 고양시 덕양구 통일로 140","tel' \
           'ephone":"070-4837-4951","bizType":"9210","bizTypeNm":"수리서비스","bizTypeDetail":"세탁소","salesCd":"K","latitude":37.0,"longitude":126' \
           '.0,"distance":null},{"totalCount":44020,"seq":4198990,"regDate":1589925661464,"simpleNm":"(주) 태정","zipCd":"10548","addr":"경기 고양시 덕' \
           '양구 서오릉로532번길 110-26","telephone":"070-4045-1168","bizType":"8499","bizTypeNm":"건강식품","bizTypeDetail":"기타건강식품","salesCd":"S",' \
           '"latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":3140406,"regDate":1519077654961,"simpleNm":"(주) 투비레어","zi' \
           'pCd":"10300","addr":"경기 고양시 일산동구 백마로 480","telephone":"031-976-2486","bizType":"2240","bizTypeNm":"문화.취미","bizTypeDetail":"애' \
           '완동물","salesCd":"8","latitude":37.661627928,"longitude":126.8015691196,"distance":null},{"totalCount":44020,"seq":3793495,"regDate":1560' \
           '895277824,"simpleNm":"(주) 피톤치드","zipCd":"10387","addr":"경기 고양시 일산서구 주화로 70","telephone":"031-1644-3714","bizType":"4499","bi' \
           'zTypeNm":"신변잡화","bizTypeDetail":"기타잡화","salesCd":"8","latitude":37.6696588557,"longitude":126.7602446141,"distance":null},{"totalCo' \
           'unt":44020,"seq":3481953,"regDate":1540850454236,"simpleNm":"(주) 허브게이트","zipCd":"10403","addr":"경기 고양시 일산동구 정발산로 24","tele' \
           'phone":"031-908-0333","bizType":"4203","bizTypeNm":"의류","bizTypeDetail":"아동의류","salesCd":"8","latitude":37.6546825345,"longitude":12' \
           '6.7726001141,"distance":null},{"totalCount":44020,"seq":4053675,"regDate":1579039259763,"simpleNm":"(주) 허브인코리아 (HUBINKOREA INC)","z' \
           'ipCd":"10335","addr":"경기 고양시 일산동구 하늘마을로 76","telephone":"031-000-0000","bizType":"9130","bizTypeNm":"용역 서비스","bizTypeDetai' \
           'l":"사무서비스","salesCd":"S","latitude":null,"longitude":null,"distance":null},{"totalCount":44020,"seq":2785615,"regDate":1505307995333,' \
           '"simpleNm":"(주) 홈비스","zipCd":"10205","addr":"경기 고양시 일산서구 덕산로195번길 188","telephone":"031-913-3001","bizType":"3102","bizType' \
           'Nm":"전기제품","bizTypeDetail":"냉열기기","salesCd":"8","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":405597' \
           '8,"regDate":1579212055741,"simpleNm":"(주)105인터내셔널","zipCd":"10447","addr":"경기 고양시 일산동구 중앙로 1048","telephone":"031-905-5010"' \
           ',"bizType":"3401","bizTypeNm":"광학제품","bizTypeDetail":"카메라","salesCd":"S","latitude":null,"longitude":null,"distance":null},{"totalC' \
           'ount":44020,"seq":2822962,"regDate":1505308118097,"simpleNm":"(주)CBM영진애드","zipCd":"10317","addr":"경기 고양시 일산동구 견달산로 245","te' \
           'lephone":"031-964-7233","bizType":"6110","bizTypeNm":"자동차정비 유지","bizTypeDetail":"자동차정비","salesCd":"A","latitude":37.6877937977,' \
           '"longitude":126.8192638648,"distance":null},{"totalCount":44020,"seq":2064008,"regDate":1505305658785,"simpleNm":"(주)PMC 오토존","zipCd":' \
           '"10225","addr":"경기 고양시 일산서구 경의로789번길 26","telephone":"031-925-8287","bizType":"6110","bizTypeNm":"자동차정비 유지","bizTypeDeta' \
           'il":"자동차정비","salesCd":"J","latitude":37.6885740169,"longitude":126.7577908244,"distance":null},{"totalCount":44020,"seq":3850276,"reg' \
           'Date":1564524058656,"simpleNm":"(주)가구프렌드","zipCd":"10595","addr":"경기 고양시 덕양구 동송로 20","telephone":"02-381-5985","bizType":"30' \
           '01","bizTypeNm":"가구","bizTypeDetail":"일반가구","salesCd":"J","latitude":37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"se' \
           'q":3727153,"regDate":1556575262973,"simpleNm":"(주)가람통상 설문동지점","zipCd":"10252","addr":"경기 고양시 일산동구 은마길 223","telephone":"' \
           '070-4282-2462","bizType":"4201","bizTypeNm":"의류","bizTypeDetail":"정장","salesCd":"K","latitude":37.0,"longitude":126.0,"distance":null}' \
           ',{"totalCount":44020,"seq":2922106,"regDate":1505308449505,"simpleNm":"(주)가야애드","zipCd":"10212","addr":"경기 고양시 일산서구 송산로 559-' \
           '17","telephone":"031-911-5793","bizType":"9101","bizTypeNm":"용역 서비스","bizTypeDetail":"종합용역","salesCd":"J","latitude":null,"longitud' \
           'e":null,"distance":null},{"totalCount":44020,"seq":3913023,"regDate":1569362457044,"simpleNm":"(주)가온메디텍","zipCd":"10437","addr":"경기 ' \
           '고양시 덕양구 호수로 100","telephone":"031-938-2230","bizType":"7040","bizTypeNm":"약국","bizTypeDetail":"제약회사","salesCd":"J","latitude":' \
           '37.0,"longitude":126.0,"distance":null},{"totalCount":44020,"seq":595996,"regDate":1505301300034,"simpleNm":"(주)가온지에스","zipCd":"10414' \
           '","addr":"경기 고양시 일산동구 중앙로 1192","telephone":"070-4141-0700","bizType":"9099","bizTypeNm":"건축자재","bizTypeDetail":"기타건축자재",' \
           '"salesCd":"J","latitude":37.6531602879,"longitude":126.7774662268,"distance":null},{"totalCount":44020,"seq":2842153,"regDate":15053081808' \
           '81,"simpleNm":"(주)감쪽가치","zipCd":"10304","addr":"경기 고양시 일산동구 은행마을로","telephone":"031-907-2928","bizType":"2215","bizTypeNm":' \
           '"문화.취미","bizTypeDetail":"민예•공예품","salesCd":"8","latitude":37.6662371816,"longitude":126.804707511,"distance":null}]}}')


def res(resp=response):
    return resp


if __name__ == '__main__':
    print(__name__)
    merchants = res()['data']['merchants']
    cnt = 0
    c = 0
    for merchant in merchants:
        c+=1
        if merchant['latitude'] is None:
            print(merchant["addr"], merchant[])
            cnt += 1

    print(c)
    print(cnt)