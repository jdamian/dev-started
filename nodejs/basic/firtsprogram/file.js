var fs = require('fs'),
    path = require('path');

var files = fs.readdirSync(path. ('./'));

fs.writeFileSync('./file.txt', files.join(','));

console.log(files);