#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

namespace Heap {
    struct KeyValue {
        int index;
        float value;
    };

    bool keyvalue_min_cmp(const KeyValue a, const KeyValue b) {
        return a.value > b.value;
    }

    int get_top_K_by_heap(const std::vector<float>& candidates, std::vector<KeyValue>& results, 
            const int results_size) {
        // copy heah K to build initialize heap
        const int candidates_size = candidates.size();
        results.resize(results_size);
        for (int i = 0; i < results_size; i++) {
            results[i].index = i;
            results[i].value = candidates[i];
        }

        // build initialize heap using head K scores O(3 * K)
        make_heap(results.begin(), results.end(), keyvalue_min_cmp);
        fprintf(stderr, "make_heap done\n");
        for (int i = 0; i < results_size; i++) {
            fprintf(stderr, "%d:%f\t", i, results[i].value);
        }
        fprintf(stderr, "\n");

        // compare top-of-heap and input data
        // push into heap and adjust, or throw out
        // O ((n-K) * log(K))
        for (int i = results_size; i < candidates_size; i++) {
            // compare top-of-heap and input data
            if (candidates[i] < results[0].value) {
                continue;
            }
            fprintf(stderr, "candidates[i]:%f results[0]:%f\n", candidates[i], results[0].value);

            fprintf(stderr, "before pop_heap\n");
            for (int j = 0; j < results_size; j++) {
                fprintf(stderr, "%d:%f\t", j, results[j].value);
            }
            fprintf(stderr, "\n");
            
            // pop before push O(2 * log(K))
            pop_heap(results.begin(), results.end(), keyvalue_min_cmp);
            results.pop_back();

            // push
            KeyValue kv = {i, candidates[i]};
            results.push_back(kv);

            // adjust O(log(K))
            push_heap(results.begin(), results.end(), keyvalue_min_cmp);
            fprintf(stderr, "push_heap done\n");
            for (int j = 0; j < results_size; j++) {
                fprintf(stderr, "%d:%f\t", j, results[j].value);
            }
            fprintf(stderr, "\n");
        }
    }

}

int main(int argc, char** argv) {
    if (2 != argc) {
        fprintf(stderr, "Usage:%s K_of_top_k", argv[0]);
        return -1;
    }
    
    int K = atoi(argv[1]);
    
    vector<float> candidates;
    string input_str;
    while(!getline(cin, input_str).eof()) {
        float num = atof(input_str.c_str());
        candidates.push_back(num);
    }
    fprintf(stderr, "read data done, candidates size:%d K:%d\n", candidates.size(), K);

    vector<Heap::KeyValue> results;
    Heap::get_top_K_by_heap(candidates, results, K);

    sort(results.begin(), results.end(), Heap::keyvalue_min_cmp);

    for (int i = 0; i < K; i++) {
        printf("%d:%d:%f\n", i, results[i].index, results[i].value);
    }
    
    return 0;
}
