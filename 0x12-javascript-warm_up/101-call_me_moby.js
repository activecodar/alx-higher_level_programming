#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
};
