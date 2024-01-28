#include <catch.hpp>
#include <cusp/complex.h>

#include <cusp/gallery/poisson.h>
#include <cusp/io/matrix_market.h>
#include <cusp/opengl/spy/spy.h>

TEST_CASE("spy", "[OpenGL]")
{
	cusp::csr_matrix<int, float, cusp::host_memory> A;
	cusp::gallery::poisson5pt(A, 500, 500);
	cusp::opengl::spy::view_matrix(A);
} // end main

