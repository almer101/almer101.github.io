#include<iostream>
#include<random>
#include <fstream> // For file handling

using namespace std;

class RandomNormalGenerator {
public:
	RandomNormalGenerator(unsigned long *seed): dist(0,1) {
		if(seed == NULL) {
			this->gen = std::default_random_engine(static_cast<unsigned>(std::time(0)));
		} else {
			this->gen = std::default_random_engine(*seed);
		}
	}
	~RandomNormalGenerator() {}

	double generate(double mean, double stdDev) {
		double z = dist(gen);
		return mean + z*stdDev;
	}

private:
	std::default_random_engine gen;
	std::normal_distribution<double> dist;
};

int main() {
	vector<vector<double> > paths;
	unsigned long seed = 14022023;
	RandomNormalGenerator generator(&seed);

	unsigned long MAX_STEP = 70000;
	double B = 1; // boundary
	double dt = 0.00025;
	double sqrt_dt = sqrt(dt);
	int N = 10000;
	unsigned long count;
	int valid_count = 0;
	double running_sum = 0;

	// open a file for writing the output
	string fileName = "simulation_output.csv";
	std::ofstream outFile(fileName);
    if (!outFile) {
        cerr << "Error opening file!" << endl;
        return 1; // Exit if the file can't be opened
    }

    // Add header
    outFile << "iter,t,value,barrier" << endl;
    int targetI = 10;

	for(int i = 0; i < N; i++) {
		// cout << "<START> <Generation:iter[" << i + 1 << "]>" << endl;
		cout << i+1 << " / " << N << "\r"; // progress bar
		
		vector<double> w;
		w.push_back(0);
		count = 0;

		if(i == targetI) {
			outFile << i+1 << "," << 0 << "," << w[w.size() - 1] << "," << B << endl;
		}

		while(w[w.size() - 1] < B && w[w.size() - 1] > -B && count < MAX_STEP) {
			double dw = generator.generate(0,sqrt_dt);
			w.push_back(w[w.size() - 1] + dw);
			count++;

			if(i == targetI) {
				outFile << i+1 << "," << dt*count << "," << w[w.size() - 1] << "," << B << endl;
			}
		}

		if(count >= MAX_STEP) continue;
		valid_count++;

		paths.push_back(w);
		running_sum += (w.size() - 1.5) * dt;
		// cout << "<END> <Generation:iter[" << i + 1 << "]>" << endl;
	}

	cout << "Average time: " << running_sum / valid_count << endl;

	outFile.close(); // Close the file
    cout << "Lines written to " << fileName << endl;

	return 0;
}