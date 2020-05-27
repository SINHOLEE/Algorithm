const dic = new Map();

dic.set('a', 1);
dic.set('b', 1);
dic.set('c', 1);

dic.delete('a');
const size = dic.clear()
console.log(size);
console.log(dic);