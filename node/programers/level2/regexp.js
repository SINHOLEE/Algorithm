function escapeRegExp(string){
    return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); // $&는 일치한 전체 문자열을 의미합니다.
  }

  console.log(escapeRegExp('asdas{d}asd{}.?^asd'));