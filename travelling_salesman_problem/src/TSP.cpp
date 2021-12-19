<<<<<<< HEAD
#include "TSP.hpp"

#include <iostream>
#include <algorithm>
#include <stack>
#include <optional>

std::ostream& operator<<(std::ostream& os, const CostMatrix& cm) {
    for (std::size_t r = 0; r < cm.size(); ++r) {
        for (std::size_t c = 0; c < cm.size(); ++c) {
            const auto& elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}

/* PART 1 */

/**
 * Create path from unsorted path and last 2x2 cost matrix.
 * @return The vector of consecutive vertex.
 */
path_t StageState::get_path() {
  reduce_cost_matrix();
  NewVertex not_last_vertex;
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    for (std::size_t c = 0; c < matrix_.size(); ++c) {
      if (matrix_[r][c] == 0)
        not_last_vertex = NewVertex(vertex_t(r, c), 0);
    }
  }
  matrix_[not_last_vertex.coordinates.row][not_last_vertex.coordinates.col] = INF;
  NewVertex last_vertex;
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    for (std::size_t c = 0; c < matrix_.size(); ++c) {
      if (matrix_[r][c] == 0)
        last_vertex = NewVertex(vertex_t(r, c), 0);
    }
  }
  unsorted_path_.insert(unsorted_path_.end(), not_last_vertex.coordinates);
  unsorted_path_.insert(unsorted_path_.end(), last_vertex.coordinates);

  path_t sorted_path;
  vertex_t prev_vertex = unsorted_path_[0];
  for (std::size_t i = 0; i < unsorted_path_.size(); ++i) {
    sorted_path.insert(sorted_path.end(), prev_vertex.col + 1);
    for (vertex_t v: unsorted_path_) {
      if (v.row == prev_vertex.col) {
        prev_vertex = v;
        break;
      }
    }
  }
  return sorted_path;
}

/**
 * Get minimum values from each row and returns them.
 * @return Vector of minimum values in row.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_rows() const {
  std::vector<cost_t> min_values;
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    auto min = INF;
    for (std::size_t c = 0; c < matrix_.size(); ++c){
      const auto &elem = matrix_[r][c];
      if (elem < min)
        min = elem;
    }
    if (is_inf(min))
      min = 0;
    min_values.insert(min_values.end(), min);
  }
  return min_values;
}

/**
 * Reduce rows so that in each row at least one zero value is present.
 * @return Sum of values reduced in rows.
 */
cost_t CostMatrix::reduce_rows() {
  cost_t sum = 0;
  std::vector<cost_t> min_values = get_min_values_in_rows();
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    for (std::size_t c = 0; c < matrix_.size(); ++c){
      if(!is_inf(matrix_[r][c]))
        matrix_[r][c] -= min_values[r];
    }
    sum += min_values[r];
  }
  return sum;
}

/**
 * Get minimum values from each column and returns them.
 * @return Vector of minimum values in columns.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {
  std::vector<cost_t> min_values;
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    auto min = INF;
    for (std::size_t c = 0; c < matrix_.size(); ++c){
      const auto &elem = matrix_[c][r];
      if (elem < min)
        min = elem;
    }
    if (is_inf(min))
      min = 0;
    min_values.insert(min_values.end(), min);
  }
  return min_values;
}

/**
 * Reduces rows so that in each column at least one zero value is present.
 * @return Sum of values reduced in columns.
 */
cost_t CostMatrix::reduce_cols() {
  cost_t sum = 0;
  std::vector<cost_t> min_values = get_min_values_in_cols();
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    for (std::size_t c = 0; c < matrix_.size(); ++c){
      if(!is_inf(matrix_[c][r]))
        matrix_[c][r] -= min_values[r];
    }
    sum += min_values[r];
  }
  return sum;
}

/**
 * Get the cost of not visiting the vertex_t (@see: get_new_vertex())
 * @param row
 * @param col
 * @return The sum of minimal values in row and col, excluding the intersection value.
 */
cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {
  cost_t min_in_row = INF;
  cost_t min_in_col = INF;
  for (std::size_t r = 0; r < matrix_.size(); ++r)
    if (r != row && matrix_[r][col] < min_in_col)
      min_in_col = matrix_[r][col];
  for (std::size_t c = 0; c < matrix_.size(); ++c)
    if (c != col && matrix_[row][c] < min_in_row)
      min_in_row = matrix_[row][c];
  return min_in_col + min_in_row;
}

/* PART 2 */

/**
 * Choose next vertex to visit:
 * - Look for vertex_t (pair row and column) with value 0 in the current cost matrix.
 * - Get the vertex_t cost (calls get_vertex_cost()).
 * - Choose the vertex_t with maximum cost and returns it.
 * @param cm
 * @return The coordinates of the next vertex.
 */
NewVertex StageState::choose_new_vertex() {
  cost_t max_cost = 0;
  vertex_t chosen_vertex;
  for (std::size_t r = 0; r < matrix_.size(); ++r) {
    for (std::size_t c = 0; c < matrix_.size(); ++c) {
      if (matrix_[r][c] == 0 && matrix_.get_vertex_cost(r, c) > max_cost) {
        max_cost = matrix_.get_vertex_cost(r, c);
        chosen_vertex.row = r;
        chosen_vertex.col = c;
      }
    }
  }
  return NewVertex(chosen_vertex, max_cost);
}

/**
 * Update the cost matrix with the new vertex.
 * @param new_vertex
 */
void StageState::update_cost_matrix(vertex_t new_vertex) {
  for (std::size_t i = 0; i < matrix_.size(); ++i) {
    matrix_[i][new_vertex.col] = INF;
    matrix_[new_vertex.row][i] = INF;
  }
  matrix_[new_vertex.col][new_vertex.row] = INF;
  unsorted_path_t path = unsorted_path_;
  while (!path.empty()) {
    std::size_t start = path[0].row;
    std::size_t end = path[0].col;
    path.erase(path.begin());
    while (!path.empty()) {
      auto start_size = path.size();
      for (std::size_t i = 0; i < path.size(); ++i) {
        if (path[i].row == end) {
          //wierzchołek do doklejenia na koniec
          end = path[i].col;
          path.erase(path.begin() + i);
        }
        if (path[i].col == start) {
          //do doklejenia na początek
          start = path[i].row;
          path.erase(path.begin() + i);
        }
      }
      if (start_size == path.size()) break;
    }
    matrix_[end][start] = INF;
  }
}

/**
 * Reduce the cost matrix.
 * @return The sum of reduced values.
 */
cost_t StageState::reduce_cost_matrix() {
  cost_t sum_in_rows = matrix_.reduce_rows();
  cost_t sum_in_cols = matrix_.reduce_cols();
  return sum_in_cols + sum_in_rows;
}

/**
 * Given the optimal path, return the optimal cost.
 * @param optimal_path
 * @param m
 * @return Cost of the path.
 */
cost_t get_optimal_cost(const path_t& optimal_path, const cost_matrix_t& m) {
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1] - 1][optimal_path[idx] - 1];
    }

    // Add the cost of returning from the last city to the initial one.
    cost += m[optimal_path[optimal_path.size() - 1] - 1][optimal_path[0] - 1];

    return cost;
}



/**
 * Create the right branch matrix with the chosen vertex forbidden and the new lower bound.
 * @param m
 * @param v
 * @param lb
 * @return New branch.
 */
StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

/**
 * Retain only optimal ones (from all possible ones).
 * @param solutions
 * @return Vector of optimal solutions.
 */
tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto& s : solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t& s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

/**
 * Solve the TSP.
 * @param cm The cost matrix.
 * @return A list of optimal solutions.
 */
tsp_solutions_t solve_tsp(const cost_matrix_t& cm) {

    StageState left_branch(cm);

    // The branch & bound tree.
    std::stack<StageState> tree_lifo;

    // The number of levels determines the number of steps before obtaining
    // a 2x2 matrix.
    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch);   // Use the first cost matrix as the root.

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    // std::cout << "1" << std::endl;

    while (!tree_lifo.empty()) {

        left_branch = tree_lifo.top();
        tree_lifo.pop();

        
        // std::cout << "2" << std::endl;

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {
            // Repeat until a 2x2 matrix is obtained or the lower bound is too high...

            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            // 1. Reduce the matrix in rows and columns.
            cost_t new_cost = left_branch.reduce_cost_matrix(); // *@TODO (KROK 1) 

            // 2. Update the lower bound and check the break condition.
            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            // 3. Get new vertex and the cost of not choosing it.
            NewVertex new_vertex = left_branch.choose_new_vertex(); // *@TODO (KROK 2)

            // 4. @TODO Update the path - use append_to_path method.
            left_branch.append_to_path(new_vertex.coordinates);

            // 5. @TODO (KROK 3) Update the cost matrix of the left branch.
            left_branch.update_cost_matrix(new_vertex.coordinates);

            // 6. Update the right branch and push it to the LIFO.
            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {
            // If the new solution is at least as good as the previous one,
            // save its lower bound and its path.
            best_lb = left_branch.get_lower_bound();
            path_t new_path = left_branch.get_path();
            solutions.push_back({get_optimal_cost(new_path, cm), new_path});
        }
    }

    return filter_solutions(solutions); // Filter solutions to find only optimal ones.
}