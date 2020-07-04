function repeatedString(s, n) {
    let res = 0;
    const MOK = parseInt(n / s.length);

    for (let i = 0; i<s.length; i++){
        if (s[i] === "a"){
            res++
        };
    };
    res *= MOK;
    for (let i = 0; i<(n % s.length);i++){
        if (s[i] === "a"){
            res++
        };
    }
    return res;
}

repeatedString("aba", 10);
