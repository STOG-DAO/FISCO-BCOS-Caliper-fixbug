import os

def fixBug647():
    # fix channelPromise.js
    os.system("mv ./node_modules/@hyperledger/caliper-fisco-bcos/lib/channelPromise.js ./node_modules/@hyperledger/caliper-fisco-bcos/lib/channelPromise.js.bak")
    os.system("cp ./fixbug#647/channelPromise.js ./node_modules/@hyperledger/caliper-fisco-bcos/lib/channelPromise.js")

    # fix fiscoBcos.js
    os.system("mv ./node_modules/@hyperledger/caliper-fisco-bcos/lib/fiscoBcos.js ./node_modules/@hyperledger/caliper-fisco-bcos/lib/fiscoBcos.js.bak")
    os.system("cp ./fixbug#647/fiscoBcos.js ./node_modules/@hyperledger/caliper-fisco-bcos/lib/fiscoBcos.js")

    # fix web3sync.js
    os.system("mv ./node_modules/@hyperledger/caliper-fisco-bcos/lib/web3lib/web3sync.js ./node_modules/@hyperledger/caliper-fisco-bcos/lib/web3lib/web3sync.js.bak")
    os.system("cp ./fixbug#647/web3sync.js ./node_modules/@hyperledger/caliper-fisco-bcos/lib/web3lib/web3sync.js")

    # fix package.json
    os.system("mv ./node_modules/@hyperledger/caliper-fisco-bcos/package.json ./node_modules/@hyperledger/caliper-fisco-bcos/package.json.bak")
    os.system("cp ./fixbug#647/package.json ./node_modules/@hyperledger/caliper-fisco-bcos/package.json")
    os.system("npm i")

if __name__ == "__main__":
    fixBug647()