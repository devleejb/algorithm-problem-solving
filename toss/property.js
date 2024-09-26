function safelyGet(obj, properties) {
  const propertyList = properties.split(".");

  if (obj === undefined) {
    return undefined;
  }

  if (propertyList.length === 1) {
    return obj[propertyList[0]];
  }

  return safelyGet(obj[propertyList[0]], propertyList.slice(1).join("."));
}

/* repository가 undefined인 경우 */
const object1 = {
  repository: undefined,
};

/* repository의 readme가 undefined인 경우 */
const object2 = {
  repository: {
    readme: undefined,
  },
};

/** repository.readme 모두가 존재하는 경우 */
const object3 = {
  repository: {
    readme: {
      extension: "md",
      content: "금융을 쉽고 간편하게",
    },
  },
};

console.log(safelyGet(object1, "repository.readme.extension"));
// -> 반환 값: undefined

console.log(safelyGet(object1, "repository.readme"));
// -> 반환 값: undefined

console.log(safelyGet(object1, "repository"));
// -> 반환 값: undefined

console.log(safelyGet(object2, "repository.readme.extension"));
// -> 반환 값: undefined

console.log(safelyGet(object2, "repository.readme"));
// -> 반환 값: undefined

console.log(safelyGet(object2, "repository"));
// -> 반환 값: { readme: undefined }

console.log(safelyGet(object3, "repository.readme.extension"));
// -> 반환 값: 'md'

console.log(safelyGet(object3, "repository.readme"));
// -> 반환 값: { extension: 'md' }
