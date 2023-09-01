//torrent-parser

import parseTorrent from 'parse-torrent';
import fs from 'fs'


async function getTorrentDetail(){

    const result = await parseTorrent(fs.readFileSync("./wibu"))
    
    console.log(result.pieces.slice(30, 30+15))
    
    //console.log(result.pieces.slice(68, 122))


}

getTorrentDetail()