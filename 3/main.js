const fs = require('fs')


let parseDiagnositcs = (rawData) => {

	//part 1
  //parse data to 2d arr
  let data = rawData.split('\n')
  data.pop()
  data = data
    .map(x => x.split(''))
    .map(x => x.map(y => parseInt(y)))

  let colSum = Array(data[0].length).fill(0)
  data.forEach(row => {
    row.forEach((x, i) => {
      colSum[i] += x
    })
  })

  let gammaBin = colSum.map(x => {
    return x >= (data.length / 2) ? 1 : 0
  })
  let epsBin = colSum.map(x => {
    return x < (data.length / 2) ? 1 : 0
  })

  let gammaRate = parseInt(gammaBin.join(''), 2)
  let epsRate = parseInt(epsBin.join(''), 2)

  console.log(gammaRate * epsRate)


  // part 2
  data = rawData.split('\n')
  data.pop()

	function mostCommon(arr, idx, roundUp=true) {
		let counts = {};
		for (const row of arr) {
			let x = row[idx]
		  counts[x] = counts[x] ? counts[x] + 1 : 1;
		}
		if (counts['0'] === counts['1']) {
			if (roundUp) {
				return '1'
			} else {
				return '0'
			}
		}
		if (roundUp) {
			return Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? a : b)
		} else {
			return Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? b : a)
		}
	}

	let curIdx = 0
	let subData = data
	while (subData.length > 1) {
		let curVal = mostCommon(subData, curIdx, true)
		subData = subData.filter(x => x[curIdx] === curVal);
		curIdx += 1
	}
	let oxy = subData[0]

	curIdx = 0
	subData = data
	while (subData.length > 1) {
		let curVal = mostCommon(subData, curIdx, false)
		subData = subData.filter(x => x[curIdx] === curVal);
		curIdx += 1
	}
	let co2 = subData[0]

	let oxyRate = parseInt(oxy, 2)
	let co2Rate = parseInt(co2, 2)
	console.log(oxyRate * co2Rate)
}

fs.readFile('input.txt', 'utf8', (err, data) => {
  parseDiagnositcs(data)
})


