## Blockchain

Blockchain is an immutable, sequential chain or records called Blocks.

They can contain transactions, files, or any data you like.

Most important fact is that they are chained together using hashes.

#### what are hash functions?

They are pretty much like a dictionary in python.

Functions that simply takes in input value, and from that input, it creates an output value.

Hash functions are generally irreversible (one-way), which means you can’t figure out the input if you only know the output – unless you try every possible input (which is called a brute-force attack).

Hash functions are often used for proving that something is the same as something else, without revealing the information beforehand. 

#### what does a block look like?

index, timestamp, list of transactions, proof, and hash of previous block.

At this point, the idea of a chain should be apparent—each new block contains within itself, the hash of the previous Block. This is crucial because it’s what gives blockchains immutability: If an attacker corrupted an earlier Block in the chain then all subsequent blocks will contain incorrect hashes.

After new_transaction() adds a transaction to the list, it returns the index of the block which the transaction will be added to—the next one to be mined. This will be useful later on, to the user submitting the transaction.

A genesis block will have the index of 1, with no previous_hash value (since its the first)

a proof is requiredwhich is the result of mining (proof of work)

#### understanding proof of work

A Proof of Work algorithm (PoW) is how new Blocks are created or mined on the blockchain. The goal of PoW is to discover a number which solves a problem. The number must be difficult to find but easy to verify—computationally speaking—by anyone on the network. This is the core idea behind Proof of Work.

