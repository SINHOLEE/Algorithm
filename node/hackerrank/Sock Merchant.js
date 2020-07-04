function sockMerchant(n, ar) {
    const bucket = new Map();

    ar.forEach(element => {
        if (bucket.get(element) === undefined){
            bucket.set(element, 1);
        } else{
            bucket.set(element, bucket.get(element) + 1);
        }
    });

    let res = 0
    bucket.forEach((val, key) => {
        res += parseInt(val / 2);
    })
    return res
}



let input = "10 20 20 10 10 30 50 10 20"
input = input.split(' ').map(item => parseInt(item, 10));
sockMerchant(9, input)