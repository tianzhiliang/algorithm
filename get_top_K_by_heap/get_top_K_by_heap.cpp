#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

namespace Heap {
    bool min_cmp(const std::pair<int, float>& a, const std::pair<int, float>& b) {
        return a.second > b.second;
    }

    bool max_cmp(const std::pair<int, float>& a, const std::pair<int, float>& b) {
        return 1 - min_cmp(a, b);
    }

    int get_top_K_by_heap(const std::vector<float>& candidates, 
            std::vector<std::pair<int, float> >& results, 
            const int results_size, bool is_increasing) {
        // copy heah K to build initialize heap
        const int candidates_size = candidates.size();
        results.resize(results_size);
        for (int i = 0; i < results_size; i++) {
            results[i].first = i;
            results[i].second = candidates[i];
        }

        // build initialize heap using head K scores O(3 * K)
        make_heap(results.begin(), results.end(), min_cmp);
        fprintf(stderr, "make_heap done\n");
        for (int i = 0; i < results_size; i++) {
            fprintf(stderr, "%d:%f\t", i, results[i].second);
        }
        fprintf(stderr, "\n");

        // compare top-of-heap and input data
        // push into heap and adjust, or throw out
        // O ((n-K) * log(K))
        for (int i = results_size; i < candidates_size; i++) {
            // compare top-of-heap and input data
            if (candidates[i] < results[0].second) {
                continue;
            }
            fprintf(stderr, "candidates[i]:%f results[0]:%f\n", candidates[i], results[0].second);

            fprintf(stderr, "before pop_heap\n");
            for (int j = 0; j < results_size; j++) {
                fprintf(stderr, "%d:%f\t", j, results[j].second);
            }
            fprintf(stderr, "\n");
            
            // pop before push O(2 * log(K))
            pop_heap(results.begin(), results.end(), min_cmp);
            results.pop_back();

            // push
            results.push_back(std::make_pair(i, candidates[i]));

            // adjust O(log(K))
            if (is_increasing) {
                push_heap(results.begin(), results.end(), max_cmp);
            } else {
                push_heap(results.begin(), results.end(), min_cmp);
            }
            fprintf(stderr, "push_heap done\n");
            for (int j = 0; j < results_size; j++) {
                fprintf(stderr, "%d:%f\t", j, results[j].second);
            }
            fprintf(stderr, "\n");
        }
    }

}

int main(int argc, char** argv) {
    if (3 != argc) {
        fprintf(stderr, "Usage:%s K_of_top_k is_increasing_order", argv[0]);
        return -1;
    }
    
    int K = atoi(argv[1]);
    int is_increasing_order = atoi(argv[2]);
    
    vector<float> candidates;
    string input_str;
    while(!getline(cin, input_str).eof()) {
        float num = atof(input_str.c_str());
        candidates.push_back(num);
    }
    fprintf(stderr, "read data done, candidates size:%d K:%d\n", candidates.size(), K);

    vector<std::pair<int, float> > results;
    Heap::get_top_K_by_heap(candidates, results, K, is_increasing_order);

    sort(results.begin(), results.end(), Heap::min_cmp);

    for (int i = 0; i < K; i++) {
        printf("%d:%d:%f\n", i, results[i].first , results[i].second);
    }
    
    return 0;
}
