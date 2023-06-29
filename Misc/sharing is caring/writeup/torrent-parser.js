//torrent-parser

import parseTorrent from 'parse-torrent';
import fs from 'fs'


async function getTorrentDetail(){

    const result = await parseTorrent(fs.readFileSync("./wibu"))
    console.log(result.pieces.slice(19, 110))
    console.log(result.pieces.slice(110, 126))


}

getTorrentDetail()