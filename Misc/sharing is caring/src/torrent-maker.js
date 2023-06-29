import createTorrent from 'create-torrent'
import fs from 'fs'

createTorrent("./hippity_hop/",{
	pieceLength:3,
	private: true,
	announceList : [[""]],
	urlList : [[""]],
},(err, torrent) => {
	if (!err) {
		fs.writeFile("wibu", torrent, (err, res) => {
			if(err) console.log(err);
		})
		}
		else{
			console.log(err);
		}
})