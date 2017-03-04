# Create shuffer data
cat ./data/feature.tagged | shuf > ./data/feature.tmp
# Divide into folds
line=`cat ./data/feature.tagged | wc -l`
fold=5
test=$(($line/$fold))
train=$(($line-$test))
# Create test and train file
head -n $test ./data/feature.tmp > ./data/test.tagged
tail -n $train ./data/feature.tmp > ./data/train.tagged
# Nothing to see here...
rm ./data/*.tmp
