#include <catch.hpp>
#include <cusp/gallery/diffusion.h>
#include <cusp/coo_matrix.h>
#include <cusp/print.h>

TEST_CASE("diffusion", "[Gallery]")
{
    cusp::coo_matrix<int, float, cusp::device_memory> A;

    // create a matrix for a diffusion problem on a 4x4 grid
    cusp::gallery::diffusion<cusp::gallery::FD>(A, 4, 4);

    // print matrix
    cusp::print(A);

}

