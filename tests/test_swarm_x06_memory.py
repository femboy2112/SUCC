"""X06 retained-memory contracts and hypothesis mutations."""
import unittest

from scripts.swarm_x06_probe import (
    assignment_oracle, bits, common_buffer, rank, report_composite,
)


class SharedBufferContract(unittest.TestCase):
    def test_strict_reusable_buffer_saving(self):
        # Independently provisioned binary buffers need four labels; two suffice jointly.
        f, g = (0, 0, 1, 2), (0, 1, 1)
        last = tuple(g[y] for y in f)
        capacity, memory, images = common_buffer((tuple(range(4)), f, last))
        self.assertEqual((rank(f), rank(g), capacity), (2, 2, 2))
        self.assertEqual(bits(capacity), 1)
        self.assertEqual(assignment_oracle(last), capacity)
        self.assertTrue(all(len(set(row)) == 4 for row in images))
        self.assertEqual(memory, (0, 1, 0, 1))

    def test_splitting_an_erased_fiber_is_rejected(self):
        # Source information cannot reappear in a claimed deterministic endpoint map.
        with self.assertRaisesRegex(ValueError, "not a function"):
            common_buffer(((0, 1), (0, 0), (0, 1)))

    def test_retained_report_changes_the_resource_contract(self):
        f, g = (0, 0), (0,)
        reported = report_composite(f, g, (0, 1), (0,))
        self.assertEqual(rank(reported), 1)
        self.assertEqual(rank(tuple(g[y] for y in f)), 2)
        self.assertEqual(common_buffer(((0, 1), reported))[0], 1)
        # Keeping an original bit in a report record has not removed that physical register.
        self.assertEqual(len(set(reported)), 2)

    def test_report_forgetting_forces_memory_back(self):
        retained = ((0, 0), (0, 1))
        forgotten = ((0,), (0,))
        capacity, _, _ = common_buffer(((0, 1), retained, forgotten))
        self.assertEqual(capacity, 2)

    def test_nonsurjectivity_blocks_reverse_local_lower_bound(self):
        f, g = (0,), (0, 0, 0)
        self.assertEqual(rank(tuple(g[y] for y in f)), 1)
        self.assertEqual(rank(g), 3)
        # Unreachable intermediate alternatives are not original-state debt.
        self.assertEqual(common_buffer(((0,), f, (0,)))[0], 1)

    def test_capacity_product_bound_is_sharp(self):
        # Four equally weighted two-element intermediate fibers merged in pairs.
        f = tuple(x // 2 for x in range(8))
        g = (0, 0, 1, 1)
        self.assertEqual(rank(tuple(g[y] for y in f)), rank(f) * rank(g))

    def test_erased_preparation_cannot_initialize_original_label(self):
        # Observer sees only e0(x)=0 and can choose a label as a function of that value.
        initial = (0, 0)
        for label in range(5):
            encoded = tuple((current, label) for current in initial)
            self.assertEqual(len(set(encoded)), 1)
        # Abstract original-dependent encoding exists, but uses unavailable original access.
        capacity, labels, images = common_buffer((initial,))
        self.assertEqual((capacity, labels), (2, (0, 1)))
        self.assertEqual(len(set(images[0])), 2)

    def test_invalid_carrier_and_capacity_contracts(self):
        for rows in ((), ((),), ((0, 1), (0,))):
            with self.assertRaises(ValueError):
                common_buffer(rows)
        for value in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                bits(value)
        with self.assertRaises(ValueError):
            report_composite((1,), (0,), (0,), (0,))


if __name__ == "__main__":
    unittest.main()
