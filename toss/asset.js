function isValid(asset) {
  if (asset.length !== 9) return false;
  const validYears = new Array(10)
    .fill(13)
    .map((year, idx) => String(year + idx));
  const year = asset.slice(0, 2);

  if (!validYears.includes(year)) return false;

  if (asset[2] !== "-") return false;

  const code = asset.slice(3, 5);
  const validCodes = ["SP", "KE", "MO", "CO", "DE"];

  if (!validCodes.includes(code)) return false;

  let validMonthCnt = 12;
  let fill = 0;

  if (year === "13") {
    validMonthCnt = 9;
    fill = 3;
  } else if (year === "22") {
    validMonthCnt = 8;
  }

  const validMonths = new Array(validMonthCnt).fill(fill).map((month, idx) => {
    let processedMonth = String(month + idx + 1);

    if (processedMonth.length !== 2) processedMonth = "0" + processedMonth;

    return processedMonth;
  });
  const month = asset.slice(5, 7);

  if (!validMonths.includes(month)) return false;

  const validSequences = new Array(99).fill(0).map((sequence, idx) => {
    let processedSequence = String(sequence + idx + 1);

    if (processedSequence.length !== 2)
      processedSequence = "0" + processedSequence;

    return processedSequence;
  });
  const sequence = asset.slice(7, 9);

  if (!validSequences.includes(sequence)) return false;

  return true;
}

function sortOption(a, b) {
  const yearA = Number(a.slice(0, 2));
  const yearB = Number(b.slice(0, 2));

  const codeOrder = ["SP", "KE", "MO", "CO", "DE"];
  const codeAIdx = codeOrder.indexOf(a.slice(3, 5));
  const codeBIdx = codeOrder.indexOf(b.slice(3, 5));

  const monthA = Number(a.slice(5, 7));
  const monthB = Number(b.slice(5, 7));

  const sequenceA = Number(a.slice(7, 9));
  const sequenceB = Number(b.slice(7, 9));

  if (yearA !== yearB) return yearA - yearB;

  if (codeAIdx !== codeBIdx) return codeAIdx - codeBIdx;

  if (monthA !== monthB) return monthA - monthB;

  if (sequenceA !== sequenceB) return sequenceA - sequenceB;
}

function solution(assets) {
  return [...new Set(assets)].filter(isValid).sort(sortOption);
}

const inputs = [
  [
    "20-DE0815",
    "20-CO1299",
    "20-MO0901",
    "20-KE0511",
    "20-SP1102",
    "21-DE0401",
    "21-CO0404",
    "21-MO0794",
    "21-KE0704",
    "21-SP0404",
    "19-DE0401",
    "19-CO0404",
    "19-MO0794",
    "19-KE1204",
    "19-SP0404",
  ],
  [
    "2-MO0915",
    "19-MO1299",
    "17-CO0901",
    "14-DE0511",
    "19-KE1102",
    "13-DE0101",
    "20-SP0404",
    "20-CO0794",
  ],
  [
    "13-DE0401",
    "13-DE0401",
    "22-MO0815",
    "19-MO1299",
    "17-CO0901",
    "14-DE0511",
    "19-KE1102",
    "20-SP0404",
    "20-CO0794",
  ],
];

const solutions = [
  [
    "19-SP0404",
    "19-KE1204",
    "19-MO0794",
    "19-CO0404",
    "19-DE0401",
    "20-SP1102",
    "20-KE0511",
    "20-MO0901",
    "20-CO1299",
    "20-DE0815",
    "21-SP0404",
    "21-KE0704",
    "21-MO0794",
    "21-CO0404",
    "21-DE0401",
  ],
  [
    "14-DE0511",
    "17-CO0901",
    "19-KE1102",
    "19-MO1299",
    "20-SP0404",
    "20-CO0794",
  ],
  [
    "13-DE0401",
    "14-DE0511",
    "17-CO0901",
    "19-KE1102",
    "19-MO1299",
    "20-SP0404",
    "20-CO0794",
    "22-MO0815",
  ],
];

for (let i = 0; i < inputs.length; ++i) {
  const result = solution(inputs[i]).every(
    (asset, idx) => asset === solutions[i][idx]
  );

  console.log(result);
}
