function printDNAHelix(length) {
    const sequence = "ATCGTTAGGG";
    let pattern = [
        "**%s%s**",
        "*%s--%s*",
        "%s----%s",
        "*%s--%s*"
    ];
    
    let seqIndex = 0;
    
    for (let i = 0; i < length; i++) {
        
        const rowPattern = pattern[i % 4];
        
        const char1 = sequence[seqIndex % sequence.length];
        const char2 = sequence[(seqIndex + 1) % sequence.length];
        seqIndex += 2;
        
        console.log(rowPattern.replace("%s", char1).replace("%s", char2));
    }
}


printDNAHelix(4);
// **AT**
// *C--G*
// T----T
// *A--G*


console.log('=================================================');


printDNAHelix(10);
// **AT**
// *C--G*
// T----T
// *A--G*
// **GG**
// *A--T*
// C----G
// *T--T*
// **AG**
// *G--G*
