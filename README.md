WordplayGen
===========

Given a word or phrase, search for similar-sounding phrases.

This requires the CMU phoneme dictionary

https://github.com/cmusphinx/cmudict/raw/master/cmudict.dict

for simple usage, and for fudging it with similar-sounding terms
it also requires the

https://github.com/cmusphinx/cmudict/raw/master/cmudict.phones

file of classifications.

Usage examples
--------------

The classic "buck an ear" punchline

    $ python wordplaygen.py "buccaneer"
    {buc,buck} {an,un} {ear}
    {buchan,buchen} {ear}
    {buccaneer}

See if fudging by one phoneme gets other possibilities:

    $ python wordplaygen.py -f 1 "buccaneer"
    {ba,bah} {can,kuhne,kun} {ear}
    {ba,bah} {keneer}
    {baack,bach,boch,bock,bohlke,bok} {an,un} {ear}
    {back,backe,bak,bakke} {an,un} {ear}
    {bakken} {ear}
    {bub,bubb} {an,un} {ear}
    {bud,budd,budde} {an,un} {ear}
    {budden} {ear}
    {bug,bugg,bugge} {an,un} {ear}
    {buc,buck} {on} {ear}
    {buc,buck} {ahn,an,ane,ann,anne} {ear}
    {buc,buck} {a,uh,uhh} {mm} {ear}
    {buc,buck} {a,uh,uhh} {knarr}
    {buc,buck} {a,uh,uhh} {knorr,nohr,nor}
    {buc,buck} {a,uh,uhh} {knerr,nair,ne'er}
    {buc,buck} {a,uh,uhh} {kneer,near,neer,nir}
    {buc,buck} {a,uh,uhh} {kneale,kneel,neal,neale,neall,neel,neil,neile,neill,niel}
    {buc,buck} {a,uh,uhh} {noir}
    {buc,buck} {a,uh,uhh} {nur}
    {buc,buck} {i'm,um,umm} {ear}
    {buc,buck} {an,un} {ahr,ar,are,our,r}
    {buc,buck} {an,un} {hors,oar,ohr,or,ore,orr}
    {buc,buck} {an,un} {hour,our}
    {buc,buck} {an,un} {eir,ire}
    {buc,buck} {an,un} {aer,air,ayre,ere,err,eyre,heir}
    {buc,buck} {an,un} {ayr}
    {buc,buck} {an,un} {ear}
    {buc,buck} {an,un} {eel}
    {buc,buck} {an,un} {uhr}
    {buc,buck} {anneal}
    {buc,buck} {ung} {ear}
    {buc,buck} {aune,on} {ear}
    {buc,buck} {ein} {ear}
    {buc,buck} {en,n} {ear}
    {buc,buck} {earn,erne,urn} {ear}
    {buc,buck} {aine,ane,ayn} {ear}
    {buc,buck} {in,in,inn} {ear}
    {buc,buck} {oanh,own} {ear}
    {buchan,buchen} {ahr,ar,are,our,r}
    {buchan,buchen} {hors,oar,ohr,or,ore,orr}
    {buchan,buchen} {hour,our}
    {buchan,buchen} {eir,ire}
    {buchan,buchen} {aer,air,ayre,ere,err,eyre,heir}
    {buchan,buchen} {ayr}
    {buchan,buchen} {ear}
    {buchan,buchen} {eel}
    {buchan,buchen} {uhr}
    {buccaneer}
    {bupp} {an,un} {ear}
    {but,butt} {an,un} {ear}
    {button} {ear}
    {baugh} {can,kuhne,kun} {ear}
    {baugh} {keneer}
    {balk} {an,un} {ear}
    {bao,bough,bow} {can,kuhne,kun} {ear}
    {bao,bough,bow} {keneer}
    {bae,bi,buy,by,bye} {can,kuhne,kun} {ear}
    {bae,bi,buy,by,bye} {keneer}
    {bike} {an,un} {ear}
    {baek,bec,beck} {an,un} {ear}
    {beckon} {ear}
    {bir,birr,bur,burr} {can,kuhne,kun} {ear}
    {bir,birr,bur,burr} {keneer}
    {berch,berk,berke,birk,bourke,burck,burk,burke} {an,un} {ear}
    {berken} {ear}
    {bay,baye,bayh,bey} {can,kuhne,kun} {ear}
    {bay,baye,bayh,bey} {keneer}
    {bake} {an,un} {ear}
    {bacon} {ear}
    {bui} {can,kuhne,kun} {ear}
    {bui} {keneer}
    {bic,bick} {an,un} {ear}
    {b,be,be,bea,bee} {can,kuhne,kun} {ear}
    {b,be,be,bea,bee} {keneer}
    {baek,beak,beeck,beek} {an,un} {ear}
    {beacon} {ear}
    {beau,beaux,bo,boe,boeh,bow,bowe} {can,kuhne,kun} {ear}
    {beau,beaux,bo,boe,boeh,bow,bowe} {keneer}
    {boak,boake,boeck,boeke,bouck} {an,un} {ear}
    {bowcan} {ear}
    {boy,boye} {can,kuhne,kun} {ear}
    {boy,boye} {keneer}
    {boik,boike} {an,un} {ear}
    {book} {an,un} {ear}
    {beu,boo} {can,kuhne,kun} {ear}
    {beu,boo} {keneer}
    {boock} {an,un} {ear}
    {dah,de,du,duh} {can,kuhne,kun} {ear}
    {dah,de,du,duh} {keneer}
    {duc,duck,duk} {an,un} {ear}
    {guck} {an,un} {ear}
    {ca} {can,kuhne,kun} {ear}
    {ca} {keneer}
    {kuc,kuck,kuk} {an,un} {ear}
    {puck} {an,un} {ear}
    {to} {can,kuhne,kun} {ear}
    {to} {keneer}
    {tuck} {an,un} {ear}

The more you fudge the phonemes, the more results you get as they
stray further from the original.

Why?
----
Because I enjoy wordplay.  So I made a tool to make it easier
when exploring language.
