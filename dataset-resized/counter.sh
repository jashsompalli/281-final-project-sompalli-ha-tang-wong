#!/bin/bash

curdir=$( pwd )
echo $curdir

touch outfile

if [ -e ${curdir}/outfile ]; then
	rm ${curdir}/outfile
	touch ${curdir}/outfile
fi

for i in $( ls ${curdir} ); do
		
	if [ -d  ${i} ]; then

		echo ${curdir}/${i}
		echo $( ls -la ${curdir}/${i}| wc -l  )

		cd ${curdir}/${i}
		for j in $( ls -tr1 ); do
			echo $(identify -format '%wx%h' ${curdir}/${i}/${j} )\ >> ${curdir}/outfile
		done
		
	fi
done

echo $( sort ${curdir}/outfile | uniq )

rm $curdir/outfile
